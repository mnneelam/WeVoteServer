# image/views_admin.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from admin_tools.views import redirect_to_sign_in_page
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages
from django.shortcuts import render
from image.controllers import cache_all_kind_of_images_locally_for_all_voter
from voter.models import fetch_voter_id_from_voter_device_link, voter_has_authority
import wevote_functions.admin
from wevote_functions.functions import convert_to_int, get_voter_api_device_id

logger = wevote_functions.admin.get_logger(__name__)


@login_required
def cache_images_locally_for_all_voters_view(request):
    authority_required = {'admin'}  # admin, verified_volunteer
    if not voter_has_authority(request, authority_required):
        return redirect_to_sign_in_page(request, authority_required)

    voter_api_device_id = get_voter_api_device_id(request)  # We look in the cookies for voter_api_device_id
    voter_id = fetch_voter_id_from_voter_device_link(voter_api_device_id)
    voter_id = convert_to_int(voter_id)

    messages_on_stage = get_messages(request)

    cache_images_locally_for_all_voters_results = cache_all_kind_of_images_locally_for_all_voter()

    template_values = {
        'messages_on_stage':                messages_on_stage,
        'cache_images_for_all_voters':      cache_images_locally_for_all_voters_results,
        'voter_id_signed_in':               voter_id
    }
    return render(request, 'image/cache_images_locally_for_all_voters.html', template_values)

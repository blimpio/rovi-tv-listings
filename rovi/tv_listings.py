from .client import RoviClient
from exceptions import RoviMissingArgumentsException

import json
import requests

BASE_URL = 'api.rovicorp.com/TVlistings/v9/listings'
SERVICES_URL = '/services'
SERVICE_DETAILS_URL = '/servicedetails'
LINEAR_SCHEDULE_URL = '/linearschedule'
GRID_SCHEDULE_URL = '/gridschedule'
PROGRAM_DETAILS_URL = '/programdetails'
CELEBRITY_DETAILS_URL = '/celebritydetails'


class TVListings(RoviClient):
    '''
    Python Wrapper for Rovi TV Listings API

    Rovi TV Listings returns international television schedules, plus data and
    images for programs and celebrities.
    '''
    def services(self, *args, **kwargs):
        '''
        Returns a list of the television service offerings for an area.
        '''
        postal_code = kwargs.get('postal_code')
        locale = kwargs.get('locale', self.locale)
        country_code = kwargs.get('country_code')
        msoid = kwargs.get('msoid')

        if None in [postal_code, country_code]:
            raise RoviMissingArgumentsException('Required Args: postal_code, country_code')

        payload = {
            'apikey': self.api_key,
            'locale': locale,
            'format': self.format,
            'countrycode': country_code
        }

        if msoid is not None:
            payload['msoid'] = msoid

        request_url = self.protocol + BASE_URL + SERVICES_URL + '/postalcode/' + postal_code + '/info'
        r = requests.get(request_url, params=payload)
        return json.loads(r.text)

    def service_details(self, *args, **kwargs):
        '''
        Returns the channel lineup offered by a television service, plus
        information about the source of programming on a channel.
        '''
        service_id = kwargs.get('service_id')
        include_channel_images = kwargs.get('include_channel_images', False)
        image_format_id = kwargs.get('image_format_id')
        image_horizontal_resolution = kwargs.get('image_horizontal_resolution')
        image_vertical_resolution = kwargs.get('image_vertical_resolution')

        if None in [service_id]:
            raise RoviMissingArgumentsException('Required Args: service_id')

        payload = {
            'apikey': self.api_key,
            'locale': self.locale,
            'format': self.format,
            'includechannelimages': int(include_channel_images)
        }

        if image_format_id is not None:
            payload['imageformatid'] = image_format_id

        if image_horizontal_resolution is not None:
            payload['imagehorizontalresolution'] = image_horizontal_resolution

        if image_vertical_resolution is not None:
            payload['imageverticalresolution'] = image_vertical_resolution

        request_url = self.protocol + BASE_URL + SERVICE_DETAILS_URL + '/serviceid/' + service_id + '/info'
        r = requests.get(request_url, params=payload)
        return json.loads(r.text)

    def linear_schedule(self, *args, **kwargs):
        '''
        TV listings with detailed program information. Fields in bold are
        required.
        '''
        service_id = kwargs.get('service_id')
        duration = kwargs.get('duration', 1)
        in_progress = kwargs.get('in_progress', False)
        one_airing_per_source_id = kwargs.get('one_airing_per_source_id', False)
        source_id = kwargs.get('source_id')
        start_date = kwargs.get('start_date')

        if None in [service_id]:
            raise RoviMissingArgumentsException('Required Args: service_id')

        payload = {
            'apikey': self.api_key,
            'locale': self.locale,
            'format': self.format,
            'duration': duration,
            'inprogress': int(in_progress),
            'oneairingpersourceid': int(one_airing_per_source_id),
        }

        if source_id is not None:
            payload['sourceid'] = source_id

        if start_date is not None:
            payload['startdate'] = start_date

        request_url = self.protocol + BASE_URL + LINEAR_SCHEDULE_URL + '/' + service_id + '/info'
        r = requests.get(request_url, params=payload)
        return json.loads(r.text)

    def grid_schedule(self, *args, **kwargs):
        '''
        TV listings designed for the space limitations of a grid.
        '''
        service_id = kwargs.get('service_id')
        duration = kwargs.get('duration', 1)
        image_format_id = kwargs.get('image_format_id')
        include_channel_images = kwargs.get('include_channel_images', False)
        source_filter_exclude = kwargs.get('source_filter_exclude')
        source_filter_include = kwargs.get('source_filter_include')
        source_id = kwargs.get('source_id')
        start_date = kwargs.get('start_date')
        title_type = kwargs.get('title_type')

        if None in [service_id]:
            raise RoviMissingArgumentsException('Required Args: service_id')

        payload = {
            'apikey': self.api_key,
            'locale': self.locale,
            'format': self.format,
            'serviceId': service_id,
            'duration': duration,
            'includechannelimages': int(include_channel_images)
        }

        if image_format_id is not None:
            payload['imageformatid'] = image_format_id

        if source_filter_exclude is not None:
            payload['sourcefilterexclude'] = source_filter_exclude

        if source_filter_include is not None:
            payload['sourcefilterinclude'] = source_filter_include

        if source_id is not None:
            payload['sourceid'] = source_id

        if start_date is not None:
            payload['startdate'] = start_date

        if title_type is not None:
            payload['titletype'] = title_type

        request_url = self.protocol + BASE_URL + GRID_SCHEDULE_URL + '/' + service_id + '/info'
        r = requests.get(request_url, params=payload)
        return json.loads(r.text)

    def program_details(self, *args, **kwargs):
        '''
        Information about a series, episode, or program, plus a schedule of
        upcoming broadcasts.
        '''
        service_id = kwargs.get('service_id')
        program_id = kwargs.get('program_id')
        copy_text_format = kwargs.get('copy_text_format', 'PlainText')
        copy_type = kwargs.get('copy_type')
        duration = kwargs.get('duration', 10080)
        image_count = kwargs.get('image_count', 5)
        image_format = kwargs.get('image_format', 'jpg')
        image_format_id = kwargs.get('image_format_id')
        image_horizontal_resolution = kwargs.get('image_horizontal_resolution')
        image_vertical_resolution = kwargs.get('image_vertical_resolution')
        image_type = kwargs.get('image_type')
        include = kwargs.get('include', 'Program')
        in_progress = kwargs.get('in_progress', True)
        page_size = kwargs.get('page_size', 0)
        source_id = kwargs.get('source_id')
        start_date = kwargs.get('start_date')

        if None in [program_id]:
            raise RoviMissingArgumentsException('Required Args: program_id')

        payload = {
            'apikey': self.api_key,
            'locale': self.locale,
            'format': self.format,
            'programId': program_id,
            'copytextformat': copy_text_format,
            'duration': duration,
            'imagecount': image_count,
            'image_format': image_format,
            'include': include,
            'inprogress': int(in_progress),
            'pagesize': page_size,
        }

        if service_id is not None:
            payload['serviceId'] = service_id

        if copy_type is not None:
            payload['copytype'] = copy_type

        if image_format_id is not None:
            payload['imageformatid'] = image_format_id

        if image_horizontal_resolution is not None:
            payload['imagehorizontalresolution'] = image_horizontal_resolution

        if image_vertical_resolution is not None:
            payload['imageverticalresolution'] = image_vertical_resolution

        if image_type is not None:
            payload['imagetype'] = image_type

        if source_id is not None:
            payload['sourceid'] = source_id

        if start_date is not None:
            payload['startdate'] = start_date

        if service_id is not None:
            request_url = self.protocol + BASE_URL + PROGRAM_DETAILS_URL + '/' + service_id + '/' + program_id + '/info'
        else:
            request_url = self.protocol + BASE_URL + PROGRAM_DETAILS_URL + '/' + program_id + '/info'
        r = requests.get(request_url, params=payload)
        return json.loads(r.text)

    def celebrity_details(self, *args, **kwargs):
        '''
        Returns information about a celebrity and can optionally include a
        schedule of upcoming broadcasts the celebrity appears in. Fields in
        bold are required.
        '''
        include = kwargs.get('include', 'All')
        name_id = kwargs.get('name_id')
        copy_text_format = kwargs.get('copy_text_format', 'PlainText')
        copy_type = kwargs.get('copy_type')
        duration = kwargs.get('duration', 10080)
        image_count = kwargs.get('image_count', 5)
        image_format = kwargs.get('image_format', 'jpg')
        image_format_id = kwargs.get('image_format_id')
        image_horizontal_resolution = kwargs.get('image_horizontal_resolution')
        image_vertical_resolution = kwargs.get('image_vertical_resolution')
        image_type = kwargs.get('image_type')
        include_credits_for_episode = kwargs.get('include_credits_for_episode', False)
        in_progress = kwargs.get('in_progress', False)
        service_id = kwargs.get('service_id')
        source_id = kwargs.get('source_id')
        start_date = kwargs.get('start_date')

        if None in [name_id]:
            raise RoviMissingArgumentsException('Required Args: name_id')

        payload = {
            'apikey': self.api_key,
            'locale': self.locale,
            'format': self.format,
            'include': include,
            'nameid': name_id,
            'copytextformat': copy_text_format,
            'duration': duration,
            'imagecount': image_count,
            'image_format': image_format,
            'include': include,
            'includecreditsforepisodes': int(include_credits_for_episode),
            'inprogress': int(in_progress),
        }

        if copy_type is not None:
            payload['copytype'] = copy_type

        if image_format_id is not None:
            payload['imageformatid'] = image_format_id

        if image_horizontal_resolution is not None:
            payload['imagehorizontalresolution'] = image_horizontal_resolution

        if image_vertical_resolution is not None:
            payload['imageverticalresolution'] = image_vertical_resolution

        if image_type is not None:
            payload['imagetype'] = image_type

        if service_id is not None:
            payload['serviceid'] = service_id

        if source_id is not None:
            payload['sourceid'] = source_id

        if start_date is not None:
            payload['startdate'] = start_date

        request_url = self.protocol + BASE_URL + CELEBRITY_DETAILS_URL + '/info'
        r = requests.get(request_url, params=payload)
        return json.loads(r.text)

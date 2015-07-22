# -*- coding: utf-8 -*-

"""airwaveapiclient.ap_graph"""


import requests
from requests.compat import urljoin
from collections import OrderedDict


class APGraph(OrderedDict):

    """Aruba networks AirWave Graph.

    Attributes:

        :url (str): AirWave URL.
        :path (str): Graph path.
        :default_start_time(int): Graph start default time.
        :default_end_time(int): Graph end default time.

    """

    def __init__(self, url, obj):
        """Initialize AirWaveAPIClient.

        Args:

            :ap_node (str): AP.

        Usage: ::

            >>> from airwaveapiclient import APGraph
            >>>

        """
        self.url = url
        self.path = '/nf/rrd_graph'
        self.default_start_time = -7200
        self.default_end_time = 0
        OrderedDict.__init__(self, obj)

    def __graph_url(self, params):
        """RRD Graph URL."""
        start = params['start']
        if not start:
            start = self.default_start_time

        end = params['end']
        if not end:
            end = self.default_end_time

        params['start'] = APGraph.graph_time_format(start)
        params['end'] = APGraph.graph_time_format(end)
        params = APGraph.urlencode(params)
        path = urljoin(self.url, self.path)
        return '%s?%s' % (path, params)

    def __ap_graph(self, graph_type, radio_type, start, end):
        """RRD access point graph base method.

        Args:

            :graph_type (str): Graph type.
            :radio_type (str): Radio type.
            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        """
        params = {}
        params['type'] = graph_type
        params['id'] = self['@id']
        if 'radio' in self:
            for radio in self['radio']:
                if 'radio_type' in radio:
                    if radio['radio_type'] == radio_type:
                        params['radio_index'] = radio['@index']
                        params['start'] = start
                        params['end'] = end
        return self.__graph_url(params)

    def client_count_802dot11bgn(self, start=None, end=None):
        """RRD graph URL for access point client count of radio type IEEE802.11BGN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.client_count_802dot11bgn(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                end=-0s&id=1&radio_index=1&start=-3600s&type=ap_client_count'

        """
        return self.__ap_graph(u'ap_client_count', u'bgn', start, end)

    def client_count_802dot11an(self, start=None, end=None):
        """RRD graph URL for access point client count of radio type IEEE802.11AN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.client_count_802dot11an(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                end=-0s&id=1&radio_index=2&start=-3600s&type=ap_client_count'

        """
        return self.__ap_graph(u'ap_client_count', u'aN', start, end)

    def bandwidth_802dot11bgn(self, start=None, end=None):
        """RRD graph URL for access point bandwidth of radio type IEEE802.11BGN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.bandwidth_802dot11bgn(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                end=-0s&id=1&radio_index=1&start=-3600s&type=ap_bandwidth'

        """
        return self.__ap_graph(u'ap_bandwidth', u'bgn', start, end)

    def bandwidth_802dot11an(self, start=None, end=None):
        """RRD graph URL for access point bandwidth of radio type IEEE802.11AN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.bandwidth_802dot11an(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                end=-0s&id=1&radio_index=2&start=-3600s&type=ap_bandwidth'

        """
        return self.__ap_graph(u'ap_bandwidth', u'aN', start, end)

    def dot11_counters_802dot11bgn(self, start=None, end=None):
        """RRD graph URL for access point dot11 counters of radio type IEEE802.11BGN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.dot11_counters_802dot11bgn(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                end=-0s&id=1&radio_index=1&start=-3600s&type=dot11_counters'

        """
        return self.__ap_graph(u'dot11_counters', u'bgn', start, end)

    def dot11_counters_802dot11an(self, start=None, end=None):
        """RRD graph URL for access point dot11 counters of radio type IEEE802.11AN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.dot11_counters_802dot11an(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                end=-0s&id=1&radio_index=2&start=-3600s&type=dot11_counters'

        """
        return self.__ap_graph(u'dot11_counters', u'aN', start, end)

    def __radio_graph(self, graph_type, radio_type, start, end):
        """RRD access point graph base method.

        Args:

            :graph_type (str): Graph type.
            :radio_type (str): Radio type.
            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        """
        params = {}
        params['type'] = graph_type
        params['ap_uid'] = self['lan_mac']
        if 'radio' in self:
            for radio in self['radio']:
                if 'radio_type' in radio:
                    if radio['radio_type'] == radio_type:
                        params['radio_index'] = radio['@index']
                        params['radio_interface'] = radio['radio_interface']
                        params['start'] = start
                        params['end'] = end
        return self.__graph_url(params)

    def radio_channel_802dot11bgn(self, start=None, end=None):
        """RRD graph URL for radio channel for radio type IEEE802.11BGN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.radio_channel_802dot11bgn(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                ap_uid=00%3A00%3A10%3A00%3A00%3A03&
                end=-0s&radio_index=1&radio_interface=2&start=-3600s&type=radio_channel'

        """
        return self.__radio_graph(u'radio_channel', u'bgn', start, end)

    def radio_channel_802dot11an(self, start=None, end=None):
        """RRD graph URL for radio channel for radio type IEEE802.11AN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.radio_channel_802dot11an(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                ap_uid=00%3A00%3A10%3A00%3A00%3A03&
                end=-0s&radio_index=2&radio_interface=1&start=-3600s&type=radio_channel'

        """
        return self.__radio_graph(u'radio_channel', u'aN', start, end)

    def radio_noise_802dot11bgn(self, start=None, end=None):
        """RRD graph URL for radio noise for radio type IEEE802.11BGN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.radio_noise_802dot11bgn(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                ap_uid=00%3A00%3A10%3A00%3A00%3A03&
                end=-0s&radio_index=1&radio_interface=2&start=-3600s&type=radio_noise'

        """
        return self.__radio_graph(u'radio_noise', u'bgn', start, end)

    def radio_noise_802dot11an(self, start=None, end=None):
        """RRD graph URL for radio noise for radio type IEEE802.11AN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.radio_noise_802dot11an(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                ap_uid=00%3A00%3A10%3A00%3A00%3A03&
                end=-0s&radio_index=2&radio_interface=1&start=-3600s&type=radio_noise'

        """
        return self.__radio_graph(u'radio_noise', u'aN', start, end)

    def radio_power_802dot11bgn(self, start=None, end=None):
        """RRD graph URL for radio power for radio type IEEE802.11BGN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.radio_power_802dot11bgn(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                ap_uid=00%3A00%3A10%3A00%3A00%3A03&
                end=-0s&radio_index=1&radio_interface=2&start=-3600s&type=radio_power'

        """
        return self.__radio_graph(u'radio_power', u'bgn', start, end)

    def radio_power_802dot11an(self, start=None, end=None):
        """RRD graph URL for radio power for radio type IEEE802.11AN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.radio_power_802dot11an(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                ap_uid=00%3A00%3A10%3A00%3A00%3A03&
                end=-0s&radio_index=2&radio_interface=2&start=-3600s&type=radio_power'

        """
        return self.__radio_graph(u'radio_power', u'aN', start, end)

    def radio_errors_802dot11bgn(self, start=None, end=None):
        """RRD graph URL for radio errors for radio type IEEE802.11BGN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.radio_errors_802dot11bgn(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                ap_uid=00%3A00%3A10%3A00%3A00%3A03&
                end=-0s&radio_index=1&radio_interface=2&start=-3600s&type=radio_errors'

        """
        return self.__radio_graph(u'radio_errors', u'bgn', start, end)

    def radio_errors_802dot11an(self, start=None, end=None):
        """RRD graph URL for radio errors for radio type IEEE802.11AN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.radio_errors_802dot11an(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                ap_uid=00%3A00%3A10%3A00%3A00%3A03&
                end=-0s&radio_index=2&radio_interface=2&start=-3600s&type=radio_errors'

        """
        return self.__radio_graph(u'radio_errors', u'aN', start, end)

    def radio_goodput_802dot11bgn(self, start=None, end=None):
        """RRD graph URL for radio goodput for radio type IEEE802.11BGN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.radio_goodput_802dot11bgn(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                ap_uid=00%3A00%3A10%3A00%3A00%3A03&
                end=-0s&radio_index=1&radio_interface=2&start=-3600s&type=radio_goodput'

        """
        return self.__radio_graph(u'radio_goodput', u'bgn', start, end)

    def radio_goodput_802dot11an(self, start=None, end=None):
        """RRD graph URL for radio goodput for radio type IEEE802.11AN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.radio_goodput_802dot11an(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                ap_uid=00%3A00%3A10%3A00%3A00%3A03&
                end=-0s&radio_index=2&radio_interface=2&start=-3600s&type=radio_goodput'

        """
        return self.__radio_graph(u'radio_goodput', u'aN', start, end)

    def channel_utilization_802dot11bgn(self, start=None, end=None):
        """RRD graph URL for channel utilization for radio type IEEE802.11BGN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.channel_utilization_802dot11bgn(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                ap_uid=00%3A00%3A10%3A00%3A00%3A03&
                end=-0s&radio_index=1&radio_interface=2&start=-3600s&type=channel_utilization'

        """
        return self.__radio_graph(u'channel_utilization', u'bgn', start, end)

    def channel_utilization_802dot11an(self, start=None, end=None):
        """RRD graph URL for channel utilization for radio type IEEE802.11AN.

        Args:

            :start (int, optional): Graph start time(seconds ago).
                Default is None.
            :end (int, optional): Graph end time(seconds ago).
                Default is None.

        Returns:

            :str: Graph URL string.

        Usage: ::

            >>> ap_graph.channel_utilization_802dot11an(start=-3600)
            'https://x.x.x.x/nf/rrd_graph?
                ap_uid=00%3A00%3A10%3A00%3A00%3A03&
                end=-0s&radio_index=2&radio_interface=2&start=-3600s&type=channel_utilization'

        """
        return self.__radio_graph(u'channel_utilization', u'aN', start, end)

    @staticmethod
    def urlencode(params):
        """URL Encode."""
        params = sorted(params.items())
        return requests.packages.urllib3.request.urlencode(params)

    @staticmethod
    def graph_time_format(seconds):
        """Graph time format."""
        return '%ss' % seconds

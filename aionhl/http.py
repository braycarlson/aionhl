import aiohttp
import asyncio
import json
import yarl
from collections import defaultdict
from .errors import (
    HTTPException,
    Forbidden,
    NotFound
)


class HTTP:
    def __init__(self, base=None, loop=None, session=None):
        self._autoclose = False
        self.base = None
        self.build = False
        self.endpoint = None
        self._loop = asyncio.get_event_loop() if loop is None else loop
        self.parameters = defaultdict(lambda: defaultdict(dict))
        self.statistics = False
        self.records = False

        if session is None:
            self._session = aiohttp.ClientSession(loop=self._loop)
            self._autoclose = True
        else:
            self._session = session

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()

    def __await__(self):
        return self.request(
            endpoint=self.endpoint,
            parameters=self.parameters,
            build=self.build
        ).__await__()

    def _process_queries(self, q):
        p = []

        for k1 in q.keys():
            v1 = q[k1]
            for v2 in v1.values():
                for k2, v3 in v2.items():
                    if v3 and v3 is not None:
                        if isinstance(v3, list):
                            if 'season' == k2:
                                start, end = v3
                                l = f'{start}{end}'
                            else:
                                l = ','.join(v3)
                            p.append(f'{k2}={l}')
                        else:
                            p.append(f'{k2}={v3}')

        return p

    def _build_queries(self, q):
        if len(q) > 1:
            if self.build:
                v1 = '+and+'.join(q)
            else:
                v1 = '&'.join(q)
        else:
            v1 = ''.join(q)

        if self.records:
            v1 = f'cayenneExp={v1}'

        return v1

    @staticmethod
    def _join_url(url, endpoint):
        return yarl.URL(url) / endpoint.lstrip('/')

    def _build_url(self, endpoint):
        return self._join_url(self.base, endpoint)

    async def request(self, **kwargs):
        endpoint = kwargs.get('endpoint')
        parameters = kwargs.get('parameters')

        parameter = self._process_queries(parameters)

        if parameter:
            path = self._build_url(endpoint)
            queries = self._build_queries(parameter)
            url = path.update_query(queries)
        else:
            url = self._build_url(endpoint)

        async with self._session.get(url) as response:
            data = await response.text(encoding='utf-8')

            if 'application/json' in response.headers:
                json.loads(data)

            if 300 > response.status >= 200:
                return data

            if response.status == 403:
                raise Forbidden(response)
            elif response.status == 404:
                raise NotFound(response)
            else:
                raise HTTPException(response)

    async def close(self):
        if self._autoclose:
            await self._session.close()

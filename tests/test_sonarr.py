# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from PyArr import SonarrAPI

@patch('PyArr.SonarrAPI.get_calendar')
def test_get_calendar(mock_get_calendar):
    calendar = [
        {
            "seriesId": 3,
            "episodeFileId": 0,
            "seasonNumber": 4,
            "episodeNumber": 11,
            "title": "Easy Com-mercial, Easy Go-mercial",
            "airDate": "2014-01-26",
            "airDateUtc": "2014-01-27T01:30:00Z",
            "overview": "To compete with fellow “restaurateur,” Jimmy Pesto, and his blowout Super Bowl event, Bob is determined to create a Bob’s Burgers commercial to air during the “big game.” In an effort to outshine Pesto, the Belchers recruit Randy, a documentarian, to assist with the filmmaking and hire on former pro football star Connie Frye to be the celebrity endorser.",
            "hasFile": false,
            "monitored": true,
            "sceneEpisodeNumber": 0,
            "sceneSeasonNumber": 0,
            "tvDbEpisodeId": 0,
            "series": {
            "tvdbId": 194031,
            "tvRageId": 24607,
            "imdbId": "tt1561755",
            "title": "Bob's Burgers",
            "cleanTitle": "bobsburgers",
            "status": "continuing",
            "overview": "Bob's Burgers follows a third-generation restaurateur, Bob, as he runs Bob's Burgers with the help of his wife and their three kids. Bob and his quirky family have big ideas about burgers, but fall short on service and sophistication. Despite the greasy counters, lousy location and a dearth of customers, Bob and his family are determined to make Bob's Burgers \"grand re-re-re-opening\" a success.",
            "airTime": "5:30pm",
            "monitored": true,
            "qualityProfileId": 1,
            "seasonFolder": true,
            "lastInfoSync": "2014-01-26T19:25:55.4555946Z",
            "runtime": 30,
            "images": [
                {
                "coverType": "banner",
                "url": "http://slurm.trakt.us/images/banners/1387.6.jpg"
                },
                {
                "coverType": "poster",
                "url": "http://slurm.trakt.us/images/posters/1387.6-300.jpg"
                },
                {
                "coverType": "fanart",
                "url": "http://slurm.trakt.us/images/fanart/1387.6.jpg"
                }
            ],
            "seriesType": "standard",
            "network": "FOX",
            "useSceneNumbering": false,
            "titleSlug": "bobs-burgers",
            "path": "T:\\Bob's Burgers",
            "year": 0,
            "firstAired": "2011-01-10T01:30:00Z",
            "qualityProfile": {
                "value": {
                "name": "SD",
                "allowed": [
                    {
                    "id": 1,
                    "name": "SDTV",
                    "weight": 1
                    },
                    {
                    "id": 8,
                    "name": "WEBDL-480p",
                    "weight": 2
                    },
                    {
                    "id": 2,
                    "name": "DVD",
                    "weight": 3
                    }
                ],
                "cutoff": {
                    "id": 1,
                    "name": "SDTV",
                    "weight": 1
                },
                "id": 1
                },
                "isLoaded": true
            },
            "seasons": [
                {
                "seasonNumber": 4,
                "monitored": true
                },
                {
                "seasonNumber": 3,
                "monitored": true
                },
                {
                "seasonNumber": 2,
                "monitored": true
                },
                {
                "seasonNumber": 1,
                "monitored": true
                },
                {
                "seasonNumber": 0,
                "monitored": false
                }
            ],
            "id": 66
            },
            "downloading": false,
            "id": 14402
        }
    ]
    # Configure the mock to return a response with an OK status code. Also, the mock should have
    # a `json()` method that returns a list of calendar entries.
    mock_get_calendar.return_value = Mock(ok=True)
    mock_get_calendar.return_value.json.return_value = calendar

    # Call the service, which will send a request to the server.
    response = get_calendar()

    # Confirm that the mock was called.
    assert_true(mock_get_calendar.called)

    # If the request is sent successfully, then I expect a response to be returned.
    assert_list_equal(response.json(), calendar)
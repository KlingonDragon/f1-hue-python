#/bin/bash
curl --request POST --header 'content-type: application/json' --url http://localhost:10101/api/graphql --data '{"query":"query ExampleQuery {liveTimingState {TrackStatus}}"}'
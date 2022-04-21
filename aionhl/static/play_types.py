play_types = [
  {
    "name": "Unknown",
    "id": "UNKNOWN",
    "cmsKey": "gamecenterUnknown",
    "playerTypes": None,
    "code": "Unknown",
    "secondaryEventCodes": []
  },
  {
    "name": "Faceoff",
    "id": "FACEOFF",
    "cmsKey": "gamecenterFaceoff",
    "playerTypes": [
      {
        "playerType": "Winner"
      },
      {
        "playerType": "Loser"
      }
    ],
    "code": "Faceoff",
    "secondaryEventCodes": []
  },
  {
    "name": "Hit",
    "id": "HIT",
    "cmsKey": "gamecenterHit",
    "playerTypes": [
      {
        "playerType": "Hitter"
      },
      {
        "playerType": "Hittee"
      }
    ],
    "code": "Hit",
    "secondaryEventCodes": []
  },
  {
    "name": "Giveaway",
    "id": "GIVEAWAY",
    "cmsKey": "gamecenterGiveaway",
    "playerTypes": [
      {
        "playerType": "PlayerID"
      }
    ],
    "code": "Giveaway",
    "secondaryEventCodes": []
  },
  {
    "name": "Goal",
    "id": "GOAL",
    "cmsKey": "gamecenterGoal",
    "playerTypes": [
      {
        "playerType": "Scorer"
      },
      {
        "playerType": "Assist"
      }
    ],
    "code": "Goal",
    "secondaryEventCodes": [
      "shot_type",
      "soResult"
    ]
  },
  {
    "name": "Shot",
    "id": "SHOT",
    "cmsKey": "gamecenterShot",
    "playerTypes": [
      {
        "playerType": "Shooter"
      },
      {
        "playerType": "Goalie"
      }
    ],
    "code": "Shot",
    "secondaryEventCodes": [
      "shot_type",
      "soResult"
    ]
  },
  {
    "name": "Missed Shot",
    "id": "MISSED_SHOT",
    "cmsKey": "gamecenterMissedShot",
    "playerTypes": [
      {
        "playerType": "Shooter"
      }
    ],
    "code": "Missed Shot",
    "secondaryEventCodes": []
  },
  {
    "name": "Penalty",
    "id": "PENALTY",
    "cmsKey": "gamecenterPenalty",
    "playerTypes": [
      {
        "playerType": "PenaltyOn"
      },
      {
        "playerType": "DrewBy"
      },
      {
        "playerType": "ServedBy"
      }
    ],
    "code": "Penalty",
    "secondaryEventCodes": [
      "pen_type"
    ]
  },
  {
    "name": "Stoppage",
    "id": "STOP",
    "cmsKey": "gamecenterStop",
    "playerTypes": None,
    "code": "Stoppage",
    "secondaryEventCodes": []
  },
  {
    "name": "Sub",
    "id": "SUB",
    "cmsKey": "gamecenterSub",
    "playerTypes": None,
    "code": "Sub",
    "secondaryEventCodes": []
  },
  {
    "name": "Fight",
    "id": "FIGHT",
    "cmsKey": "gamecenterFight",
    "playerTypes": [
      {
        "playerType": "Fighter"
      }
    ],
    "code": "Fight",
    "secondaryEventCodes": []
  },
  {
    "name": "Takeaway",
    "id": "TAKEAWAY",
    "cmsKey": "gamecenterTakeaway",
    "playerTypes": [
      {
        "playerType": "PlayerID"
      }
    ],
    "code": "Takeaway",
    "secondaryEventCodes": []
  },
  {
    "name": "Blocked Shot",
    "id": "BLOCKED_SHOT",
    "cmsKey": "gamecenterBlockedShot",
    "playerTypes": [
      {
        "playerType": "Blocker"
      },
      {
        "playerType": "Shooter"
      }
    ],
    "code": "Blocked Shot",
    "secondaryEventCodes": []
  },
  {
    "name": "Period Start",
    "id": "PERIOD_START",
    "cmsKey": "gamecenterPeriodStart",
    "playerTypes": None,
    "code": "Period Start",
    "secondaryEventCodes": []
  },
  {
    "name": "Period End",
    "id": "PERIOD_END",
    "cmsKey": "gamecenterPeroidEnd",
    "playerTypes": None,
    "code": "Period End",
    "secondaryEventCodes": []
  },
  {
    "name": "Game End",
    "id": "GAME_END",
    "cmsKey": "gamecenterGameEnd",
    "playerTypes": None,
    "code": "Game End",
    "secondaryEventCodes": []
  },
  {
    "name": "Game Scheduled",
    "id": "GAME_SCHEDULED",
    "cmsKey": "gamecenterGameScheduled",
    "playerTypes": None,
    "code": "Game Scheduled",
    "secondaryEventCodes": []
  },
  {
    "name": "Period Ready",
    "id": "PERIOD_READY",
    "cmsKey": "gamecenterPeroidReady",
    "playerTypes": None,
    "code": "Period Ready",
    "secondaryEventCodes": []
  },
  {
    "name": "Period Official",
    "id": "PERIOD_OFFICIAL",
    "cmsKey": "gamecenterPeiodOfficial",
    "playerTypes": None,
    "code": "Period Official",
    "secondaryEventCodes": []
  },
  {
    "name": "Shootout Complete",
    "id": "SHOOTOUT_COMPLETE",
    "cmsKey": "gamecenterShootoutComplete",
    "playerTypes": None,
    "code": "Shootout Complete",
    "secondaryEventCodes": []
  },
  {
    "name": "Early Intermission Start",
    "id": "EARLY_INT_START",
    "cmsKey": "gamecenterEarlyIntermissionStart",
    "playerTypes": None,
    "code": "Early Intermission Start",
    "secondaryEventCodes": []
  },
  {
    "name": "Early Intermission End",
    "id": "EARLY_INT_END",
    "cmsKey": "gamecenterEarlyIntermissionEnd",
    "playerTypes": None,
    "code": "Early Intermission End",
    "secondaryEventCodes": []
  },
  {
    "name": "Game Official",
    "id": "GAME_OFFICIAL",
    "cmsKey": "gamecenterGameOfficial",
    "playerTypes": None,
    "code": "Game Official",
    "secondaryEventCodes": []
  },
  {
    "name": "Official Challenge",
    "id": "CHALLENGE",
    "cmsKey": "gamecenterOfficialChallenge",
    "playerTypes": None,
    "code": "Official Challenge",
    "secondaryEventCodes": []
  },
  {
    "name": "Emergency Goaltender",
    "id": "EMERGENCY_GOALTENDER",
    "cmsKey": "gamecenterEmergencyGoaltender",
    "playerTypes": None,
    "code": "Emergency Goaltender Player ID Change",
    "secondaryEventCodes": []
  }
]

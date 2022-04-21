import asyncio

from aionhl.statistics.awards import Awards
from aionhl.statistics.conferences import Conferences
from aionhl.statistics.divisions import Divisions
from aionhl.statistics.draft import Drafts
from aionhl.statistics.games import Games
from aionhl.statistics.players import Players
from aionhl.statistics.prospects import Prospects
from aionhl.statistics.schedules import Schedules
from aionhl.statistics.seasons import Seasons
from aionhl.statistics.standings import Standings
from aionhl.statistics.teams import Teams
from aionhl.statistics.tournaments import Tournaments
from aionhl.statistics.venues import Venues

from aionhl.records.attendance import AttendanceRecords
from aionhl.records.drafts import DraftRecords
from aionhl.records.franchises import FranchiseRecords
from aionhl.records.milestones import MilestoneRecords
from aionhl.records.officials import OfficialRecords
from aionhl.records.players import PlayerRecords
from aionhl.records.playoffs import PlayoffRecords
from aionhl.records.records import Records
from aionhl.records.trophies import TrophyRecords


async def main():
    async with AttendanceRecords() as attendance:
        data = await attendance.get()
        print(data)

    async with DraftRecords() as drafts:
        data = await drafts.get(
            team=18,
            year=2015
        )

        data = await drafts.get(year=2016)
        data = await drafts.get()
        print(data)

    async with FranchiseRecords() as franchises:
        data = await franchises.get(
         franchise=3,
         season=2,
         order='desc'
        )

        data = await franchises.get_details(
         franchise=3,
         season=2,
         order='desc'
        )

        data = await franchises.get_season_records(
         franchise=3,
         season=2,
         order='desc'
        )

        data = await franchises.get_season_results(
         franchise=3,
         season=2,
         order='desc'
        )

        data = await franchises.get_team_records(
         franchise=3,
         season=2,
         order='desc'
        )

        data = await franchises.get_goalie_records(
         franchise=3,
         season=2,
         order='desc'
        )

        data = await franchises.get_skater_records(
         franchise=3,
         season=2,
         order='desc'
        )

        print(data)

    async with MilestoneRecords() as milestones:
        data = await milestones.get_one_thousand_point_career()
        data = await milestones.get_five_hundred_goal_career()
        data = await milestones.get_one_hundred_point_season()
        data = await milestones.get_fifty_goal_season()
        data = await milestones.get_five_goal_game()

        print(data)

    async with OfficialRecords() as officials:
        data = await officials.get()
        data = await officials.get(active=False)
        data = await officials.get(active=True)

        print(data)

    async with PlayerRecords() as players:
        data = await players.get()
        data = await players.get_by(team_id=16)

        print(data)

    async with PlayoffRecords() as playoffs:
        data = await playoffs.get(
             series='Stanley Cup Final',
             season=['2017', '2018']
         )
        data = await playoffs.get(
             series='Stanley Cup Final'
         )
        data = await playoffs.get(
             season=['2015', '2017']
         )

        print(data)

    async with Records() as records:
        data = await records.get_detail(franchise=3, gametype=2)
        data = await records.get_all_time(franchise=3, gametype=2)
        data = await records.get_playoff(franchise=3, gametype=2)

        print(data)

    async with TrophyRecords() as trophies:
        data = await trophies.get()

        print(data)

    async with Awards() as awards:
        data = await awards.get()
        data = await awards.get_by(id=24)

        print(data)

    async with Conferences() as conferences:
        data = await conferences.get()
        data = await conferences.get_by(id=5)

        print(data)

    async with Divisions() as divisions:
        data = await divisions.get()
        data = await divisions.get_by(id=5)

        print(data)

    async with Drafts() as drafts:
        data = await drafts.get()
        data = await drafts.get_by(start=2018, end=2019)

        print(data)

    async with Games() as games:
        data = await games.get_feed(game=3)
        data = await games.get_boxscore(game=3)
        data = await games.get_linescore(game=3)
        data = await games.get_content(game=3)

        print(data)

    async with Players() as players:
        data = await players.get_information(player='8477934')

        data = await players.get_statistics(
            player='8477934',
            year=True,
            playoff=['2017', '2018'],
        )

        print(data)

    async with Prospects() as prospects:
        data = await prospects.get()
        data = await prospects.get_by(id=51656)

        print(data)

    async with Schedules() as schedules:
        data = await schedules.get(
            broadcast=True,
            linescore=True,
            team=['16', '18'],
            gametype='R'
        )

        print(data)

    async with Seasons() as seasons:
        data = await seasons.get()
        data = await seasons.get_current()
        data = await seasons.get_by(start=2017, end=2018)

        print(data)

    async with Standings() as standings:
        data = await standings.get_wildcards(
            season=['2016', '2017'],
            record=True
        )

        print(data)

    async with Teams() as teams:
        data = await teams.get(
            team=['10', '18'],
            roster=['2011', '2012'],
            name=True,
            statistics=True
        )

        print(data)

    async with Tournaments() as tournaments:
        data = await tournaments.get(
            season=['2018', '2019'],
            round=True
        )
        data = await tournaments.get(
            round=True
        )
        data = await tournaments.get(
            season=['2018', '2019']
        )

        print(data)

    async with Venues() as venues:
        data = await venues.get()
        data = await venues.get_by(id=3)

        print(data)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.stop()

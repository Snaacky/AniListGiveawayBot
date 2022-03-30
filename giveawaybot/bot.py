import argparse
import json
import random

import requests
from loguru import logger


class AniListGiveaway:
    def __init__(self, args):
        self.args = args
        logger.info(f"Getting contestents from '{self.args.user}' followers list")
        self.contestents = self.get_contestents()
        logger.info(f"Found {len(self.contestents)} contestents")
        self.winners = self.draw_winners()
        logger.info(f"Winner(s): {', '.join(self.winners)}")

    def get_contestents(self):
        query = """
        query ($page: Int, $userId: Int!) {
            Page(page: $page) {
                pageInfo {
                total
                perPage
                currentPage
                lastPage
                hasNextPage
                }
                followers(userId: $userId, sort: USERNAME) {
                name
                }
            }
        }
        """
        contestents = []
        page = 1
        while True:
            variables = {"userId": self.args.user, "page": page}
            r = requests.post(
                url="https://graphql.anilist.co/",
                json={"query": query, "variables": variables},
            )

            try:
                r = r.json()
            except json.JSONDecodeError:
                logger.error(
                    f"Failed to get API data for user '{variables['userId']}': {r.text}"
                )
                raise SystemExit

            if self.args.debug:
                logger.debug(f"GraphQL API response: {r}")

            if "errors" in r.keys():
                for message in r["errors"]:
                    logger.error(f"GraphQL API returned an error: {message['message']}")
                raise SystemExit

            if not r["data"]["Page"]["followers"]:
                logger.error(
                    "Either the AniList user ID specified was invalid or the user has no followers"
                )

            if len(r["data"]["Page"]["followers"]) < self.args.winners:
                logger.error(
                    "The amount of winners to be drawn is higher than the amount of followers"
                )
                raise SystemExit

            for user in r["data"]["Page"]["followers"]:
                contestents.append(user["name"])

            if page >= r["data"]["Page"]["pageInfo"]["lastPage"]:
                break

            page += 1

        return contestents

    def draw_winners(self):
        return random.sample(population=self.contestents, k=self.args.winners)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u",
        "--user",
        help="The ID of the user to draw contesents from",
        type=int,
        required=True,
    )
    parser.add_argument(
        "-w",
        "--winners",
        help="The amount of winners to be drawn",
        type=int,
        required=True,
    )
    parser.add_argument(
        "-d",
        "--debug",
        help="Run the script in debug mode, logs extra information to console",
        action="store_true",
        required=False,
    )
    args = parser.parse_args()
    AniListGiveaway(args)

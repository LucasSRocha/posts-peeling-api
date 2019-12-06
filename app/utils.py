from typing import Tuple, List

from requests import get


def get_user_info(user_email: str) -> Tuple[bool, dict]:
    """
    This function is used to get the general information about a user using the e-mail registered
    :param user_email: str
    :return: Tuple[bool, dict] >> True, { .... user details ...}
    """
    url = f'https://jsonplaceholder.typicode.com/users?email={user_email}'

    response = get(url)

    if response.status_code == 200 and response.json():
        return True, response.json()[0]

    return False, {}


def get_user_posts(user_id: str) -> List[dict]:
    """
    This function is used to obtain all posts related to a userId.
    :param user_id: str
    :return: List[dict} >> [{... post ...}, {...post2...}]
    """
    url = f'https://jsonplaceholder.typicode.com/posts?userId={user_id}'

    json_data = [{}]

    response = get(url)

    if response.status_code == 200:
        json_data = response.json()

    return json_data


def format_index_response(user_info: dict, user_posts: List[dict]) -> dict:
    """
    This function formats the response accordingly as the defined standard.
    :param user_info: dict -> general user info
    :param user_posts: List[dict] -> posts related to user
    :return: dict -> formatted dict response
    """
    response_dict = dict()

    response_dict['user'] = user_info

    # remove all userId's from the posts
    [post.pop('userId', None) for post in user_posts]

    response_dict['posts'] = user_posts

    return response_dict


def resolve_posts_lookup(user_email: str) -> Tuple[dict, int]:
    """
    This function centralizes the logic behind the requests and process it.

    :param user_email: str -> registered user e-mail
    :return: Tuple[dict, int] -> response dict, status_code obtained while processing the e-mail requested
    """
    if not user_email:
        return {'response': 'User not Informed'}, 400

    valid_user, user_info = get_user_info(user_email=user_email)

    if not valid_user:
        return {'response': 'User not found'}, 404

    user_posts = get_user_posts(user_info.get('id'))

    formatted_response = format_index_response(user_info=user_info, user_posts=user_posts)

    return {'response': formatted_response}, 200

import grequests
from usernames_handler import get_usernames
from profile_handler import (
    get_pinned_repos,
    get_repos,
    has_email,
    has_linkedin,
    get_sidebar,
)
from readme_handler import get_readme, get_tags
from image_processing import has_photo


def populate_dict(user_dict):
    user_dict["readme"] = get_readme(user_dict["github_readme"])
    user_dict["sidebar"] = get_sidebar(user_dict["github"])
    user_dict["linkedin"] = has_linkedin(user_dict["sidebar"], user_dict["readme"])
    user_dict["email"] = has_email(user_dict["sidebar"], user_dict["readme"])
    user_dict["tags"] = get_tags(user_dict["github_readme"])
    user_dict["repos"] = get_repos(user_dict["github"])
    user_dict["pinned"] = get_pinned_repos(user_dict["github"])

    return user_dict


def populate_dicts(list_of_dicts):

    counter = 0
    for each_dict in list_of_dicts:
        populate_dict(each_dict)
        counter += 1
        print(f"pessoa #{counter} de {len(list_of_dicts)}")

    return list_of_dicts

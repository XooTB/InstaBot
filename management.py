from instapy import InstaPy
import Bot


def createSession(username, password):
    Session = InstaPy(username, password,
                      headless_browser=False, multi_logs=True)
    return Session


def Follow(Session, Type, List, Amount, Intract):
    Session.login()
    if Type.lower() == 'fbu':
        Bot.followByUsers(Session, List, Amount, Intract)
    elif Type.lower() == 'fbt':
        Bot.followByTags(Session, List, Amount, Intract)
    elif Type.lower() == 'flbu':
        Bot.followByUsernames(Session, List, Amount, Intract)


def takeData(List=False, Amount=False, Intract=False):
    Dlist = []
    if List:
        Dlist = input(
            'Enter the List of Tags/Usernames you want to Follow/Unfollow, Separated by ",": ').split(',')
    IAmount = 10
    if Amount:
        IAmount = input(
            'Enter the Amount You want to be Followed/Unfollowed: ')
    intract = False
    if Intract:
        intract = bool(
            int(input('Do you want to Intract witht the Users? Enter 1 for YES 0 for NO: ')))

    return [Dlist, IAmount, intract]


def unfollow(Session, Type, List, Amount, Intract):
    Session.login()
    if Type == 'unf':
        Bot.unfollowNonFollowers(Session, Amount)
    elif Type == 'ubu':
        Bot.unfollowByUsernames(Session, List, Amount)
    elif Type == 'ufi':
        Bot.unfollowInstapyFollowed(Session, Amount)
    elif Type == 'ufr':
        Bot.unfollowRandom(Session, Amount)


def like(Session, Type, List, Amount, Intract):
    if Type == 'lbh':
        Bot.likeByHashtags(Session, List, Amount, Intract)
    elif Type == 'lof':
        Bot.likeOnFeed(Session, Amount, Intract)

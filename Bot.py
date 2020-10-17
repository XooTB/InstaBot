from instapy import InstaPy

# Follow User Following.. follow the Followers of a Specifice User


def followByUsers(Session, Ulist=[], amount=10, intract=False):
    Session.follow_user_following(Ulist, amount=amount, interact=intract)

# Follow by Hastags


def followByTags(Session, Tlist=[], amount=10, intract=False):
    Session.follow_by_tags(Tlist, amount, interact=intract)

# follow by UserNames


def followByUsernames(Session, Ulist=[], amount=10, intract=False):
    Session.follow_by_list(Ulist, amount, 60*3, intract)

# Unfollow users by list


def unfollowByUsernames(Session, Ulist=[], amount=10):
    Session.unfollow_users(
        amount=amount, custom_list_enabled=True, custom_list=Ulist)

# Unfollow Nonfollowers


def unfollowNonFollowers(Session, amount=10):
    Session.unfollow_users(amount=amount, nonFollowers=True,
                           allFollowing=False, instapy_followed_enabled=False)

# Unfollow Instapy Following


def unfollowInstapyFollowed(Session, amount=10):
    Session.unfollow_users(amount=amount, nonFollowers=False,
                           allFollowing=False, instapy_followed_enabled=True)

# Unfollow Randomly


def unfollowRandom(Session, amount=10):
    Session.unfollow_users(amount=amount, nonFollowers=False,
                           allFollowing=True, instapy_followed_enabled=False)

# Like By Hastags


def likeByHashtags(Session, Tlist=[], amount=10, intract=False):
    Session.like_by_tags(Tlist, amount, intract=intract)


# likes Posts on your Feed


def likeOnFeed(Session, amount=10, intract=False):
    Session.like_by_feed(amount=amount, unfollow=False, intract=intract)

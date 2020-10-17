from instapy import InstaPy
import management as man


FollowMenu = ['1: Follow from Users',
              '2: Follow by TAGS',
              '3: Follow by Usernames']

UnfollowMenu = ['1: Unfollow Randomly',
                '2: Unfollow Non Followers',
                '3: Followers Followed by InstaBOT',
                '4: Unfollow Specifiq Users']

LikeMenu = ['1: Like by Hastags',
            '2: Like From Feed']

# take username and Passowrd
print('Welcome to InstaBOT \nPlease Enter your Username and Password!')

userName = input('Username: ')
Password = input('Password: ')


print('Thanks! What do you want to do?: Follow, Unfollow, Like: ', end='')
task = input().lower()


'''
Following Part
'''

if task == 'follow':
    for i in FollowMenu:
        print(i)
    num = input('Enter the number of the task you want to do: ')
    if num == '1':
        data = man.takeData(True, True, True)
        man.Follow(man.createSession(userName, Password),
                   'fbu', data[0], data[1], data[2])
    elif num == '2':
        data = man.takeData(True, True, True)
        man.Follow(man.createSession(userName, Password),
                   'fbt', data[0], data[1], data[2])
    elif num == '3':
        data = man.takeData(True, True, True)

'''
Unfollowing Part
'''

if task == 'unfollow':
    for i in UnfollowMenu:
        print(i)
    num = input('Enter the Task you want to do: ')
    if num == '1':
        data = man.takeData(0, 1, 0)
        man.unfollow(man.createSession(userName, Password),
                     'ufr', False, True, False)
    elif num == '2':
        data = man.takeData(Amount=True)
        man.unfollow(man.createSession(userName, Password),
                     'unf', False, data[1], False)
    elif num == '3':
        data = man.takeData(Amount=True)
        man.unfollow(man.createSession(userName, Password),
                     'ufi', False, data[1], False)
    elif num == '4':
        data = man.takeData(True, True, False)
        man.unfollow(man.createSession(userName, Password),
                     'ufu', data[0], data[1], False)


'''
Liking Part
'''

if task == 'like':
    for i in LikeMenu:
        print(i)
    num = input('What do you want to do?: ')
    if num == '1':
        data = man.takeData(True, True, True)
        man.like(man.createSession(userName, Password),
                 'lbh', data[0], data[1], data[2])
    elif num == '2':
        data = man.takeData(False, True, True)
        man.like(man.createSession(userName, Password),
                 'lof', False, data[1], data[2])

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from friendship.models import Friend, FriendshipRequest

from takes.models import Take


class Command(BaseCommand):
    help = "Creates some Users and Takes creates Demo environment"

    def handle(self, *args, **options):
        # cascading will delete all other users too
        User.objects.exclude(username='admin').delete()

        # showcase user
        demo = User.objects.create_user('Demo', 'demo@mail.de', 'user0921')

        # Credits: GPT :)
        peter = User.objects.create_user('Peter', 'peter@mail.de', 'user0921')
        hans = User.objects.create_user('Hans', 'hans@mail.de', 'user0921')
        max = User.objects.create_user('Max', 'max@mail.de', 'user0921')
        jane = User.objects.create_user('Jane', 'jane@mail.de', 'user0921')
        john = User.objects.create_user('John', 'john@mail.de', 'user0921')
        alice = User.objects.create_user('Alice', 'alice@mail.de', 'user0921')
        bob = User.objects.create_user('Bob', 'bob@mail.de', 'user0921')
        clara = User.objects.create_user('Clara', 'clara@mail.de', 'user0921')
        david = User.objects.create_user('David', 'david@mail.de', 'user0921')
        emma = User.objects.create_user('Emma', 'emma@mail.de', 'user0921')
        frank = User.objects.create_user('Frank', 'frank@mail.de', 'user0921')
        grace = User.objects.create_user('Grace', 'grace@mail.de', 'user0921')
        henry = User.objects.create_user('Henry', 'henry@mail.de', 'user0921')
        irene = User.objects.create_user('Irene', 'irene@mail.de', 'user0921')

        Friend.objects.create(to_user=peter, from_user=max)
        Friend.objects.create(to_user=hans, from_user=jane)
        Friend.objects.create(to_user=alice, from_user=john)
        Friend.objects.create(to_user=bob, from_user=clara)
        Friend.objects.create(to_user=david, from_user=emma)
        Friend.objects.create(to_user=frank, from_user=grace)
        Friend.objects.create(to_user=henry, from_user=irene)
        Friend.objects.create(to_user=emma, from_user=jane)
        Friend.objects.create(to_user=clara, from_user=henry)
        Friend.objects.create(to_user=irene, from_user=peter)
        Friend.objects.create(to_user=max, from_user=alice)
        Friend.objects.create(to_user=john, from_user=hans)
        Friend.objects.create(to_user=grace, from_user=bob)

        # create some open friend requests
        FriendshipRequest.objects.create(from_user=peter, to_user=demo)
        FriendshipRequest.objects.create(from_user=grace, to_user=demo)
        FriendshipRequest.objects.create(from_user=alice, to_user=demo)
        FriendshipRequest.objects.create(from_user=max, to_user=demo)
        FriendshipRequest.objects.create(from_user=john, to_user=demo)

        # Generative AI shines at this task, love it
        # Initial Takes
        peterTake1 = Take.objects.create(author=peter, content='I love swimming', reply_to=None)
        hansTake1 = Take.objects.create(author=hans, content='Reading is my favorite hobby',
                                        reply_to=None)
        maxTake1 = Take.objects.create(author=max, content='Coding is life!', reply_to=None)
        janeTake1 = Take.objects.create(author=jane, content='Cooking is an art', reply_to=None)
        johnTake1 = Take.objects.create(author=john, content='I enjoy hiking', reply_to=None)

        # Replies to initial Takes
        aliceTake1 = Take.objects.create(author=alice, content='I agree with you, Peter!', reply_to=peterTake1)
        bobTake1 = Take.objects.create(author=bob, content='Reading is great, Hans!', reply_to=hansTake1)
        claraTake1 = Take.objects.create(author=clara, content='Yes, coding is amazing, Max!', reply_to=maxTake1)
        davidTake1 = Take.objects.create(author=david, content='I love cooking too, Jane!', reply_to=janeTake1)
        emmaTake1 = Take.objects.create(author=emma, content='Hiking is fun, John!', reply_to=johnTake1)

        # More Takes without replies
        frankTake1 = Take.objects.create(author=frank, content='Music is my passion', reply_to=None)
        graceTake1 = Take.objects.create(author=grace, content='Dancing is my life', reply_to=None)
        henryTake1 = Take.objects.create(author=henry, content='Traveling the world is my dream', reply_to=None)
        ireneTake1 = Take.objects.create(author=irene, content='I enjoy painting', reply_to=None)

        # Replies to replies
        peterTake2 = Take.objects.create(author=peter, content='Thanks, Alice!', reply_to=aliceTake1)
        hansTake2 = Take.objects.create(author=hans, content='Glad you think so, Bob!', reply_to=bobTake1)
        maxTake2 = Take.objects.create(author=max, content='Absolutely, Clara!', reply_to=claraTake1)
        janeTake2 = Take.objects.create(author=jane, content='Cooking is wonderful, David!', reply_to=davidTake1)
        johnTake2 = Take.objects.create(author=john, content='Hiking is the best, Emma!', reply_to=emmaTake1)

        # More replies to initial Takes
        aliceTake2 = Take.objects.create(author=alice, content='Swimming is fun, Peter!', reply_to=peterTake1)
        bobTake2 = Take.objects.create(author=bob, content='Books are a great escape, Hans!', reply_to=hansTake1)
        claraTake2 = Take.objects.create(author=clara, content='Coding is creativity, Max!', reply_to=maxTake1)
        davidTake2 = Take.objects.create(author=david, content='Cooking brings joy, Jane!', reply_to=janeTake1)
        emmaTake2 = Take.objects.create(author=emma, content='Hiking is peaceful, John!', reply_to=johnTake1)

        # Even more Takes
        frankTake2 = Take.objects.create(author=frank, content='Music transcends languages', reply_to=None)
        graceTake2 = Take.objects.create(author=grace, content='Dancing is a universal language', reply_to=None)
        henryTake2 = Take.objects.create(author=henry, content='I want to visit every continent', reply_to=None)
        ireneTake2 = Take.objects.create(author=irene, content='Painting is my therapy', reply_to=None)

        # Replies to replies of replies
        peterTake3 = Take.objects.create(author=peter, content='Let\'s go swimming together, Alice!', reply_to=aliceTake2)
        hansTake3 = Take.objects.create(author=hans, content='Bob, what\'s your favorite book?', reply_to=bobTake2)
        maxTake3 = Take.objects.create(author=max, content='Clara, what\'s your favorite coding language?', reply_to=claraTake2)
        janeTake3 = Take.objects.create(author=jane, content='David, share your best recipe!', reply_to=davidTake2)
        johnTake3 = Take.objects.create(author=john, content='Emma, where\'s your favorite hiking spot?', reply_to=emmaTake2)

        # More Takes
        aliceTake3 = Take.objects.create(author=alice, content='Swimming is so refreshing!', reply_to=None)
        bobTake3 = Take.objects.create(author=bob, content='Reading expands the mind', reply_to=None)
        claraTake3 = Take.objects.create(author=clara, content='Coding solves problems', reply_to=None)
        davidTake3 = Take.objects.create(author=david, content='Cooking for loved ones is the best', reply_to=None)
        emmaTake3 = Take.objects.create(author=emma, content='Hiking brings me peace', reply_to=None)

        # Additional replies to initial Takes
        frankTake3 = Take.objects.create(author=frank, content='Peter, do you swim often?', reply_to=peterTake1)
        graceTake3 = Take.objects.create(author=grace, content='Hans, what genre do you like to read?', reply_to=hansTake1)
        henryTake3 = Take.objects.create(author=henry, content='Max, do you code professionally?', reply_to=maxTake1)
        ireneTake3 = Take.objects.create(author=irene, content='Jane, what\'s your favorite dish to cook?', reply_to=janeTake1)

        # More replies to replies of replies
        peterTake4 = Take.objects.create(author=peter, content='Alice, swimming is the best workout!', reply_to=aliceTake3)
        hansTake4 = Take.objects.create(author=hans, content='Bob, I love fantasy novels!', reply_to=bobTake3)
        maxTake4 = Take.objects.create(author=max, content='Clara, Python is my favorite!', reply_to=claraTake3)
        janeTake4 = Take.objects.create(author=jane, content='David, my secret ingredient is love!', reply_to=davidTake3)
        johnTake4 = Take.objects.create(author=john, content='Emma, hiking in the mountains is amazing!', reply_to=emmaTake3)

        # New initial Takes
        gpt_peterTake2 = Take.objects.create(author=peter, content='Nature is calming', reply_to=None)
        gpt_hansTake2 = Take.objects.create(author=hans, content='I enjoy painting', reply_to=None)
        gpt_maxTake2 = Take.objects.create(author=max, content='Music soothes the soul', reply_to=None, is_public=False)
        gpt_janeTake2 = Take.objects.create(author=jane, content='I love gardening', reply_to=None)
        gpt_johnTake2 = Take.objects.create(author=john, content='Baking is my passion', reply_to=None, is_public=False)
        gpt_aliceTake2 = Take.objects.create(author=alice, content='Traveling is life', reply_to=None)

        gpt_maxTake2_ = Take.objects.create(author=max, content='Gaming is fun!', reply_to=None, is_public=False)
        gpt_johnTake2_ = Take.objects.create(author=john, content='Baking cake is my passion', reply_to=None, is_public=False)
        gpt_davidTake3_ = Take.objects.create(author=john, content='Mastery in baking comes with practice', reply_to=None, is_public=False)  # David and Max are friends

        # New Replies (some are private)
        gpt_bobTake2 = Take.objects.create(author=bob, content='Absolutely, nature is wonderful!', reply_to=gpt_peterTake2)
        gpt_claraTake2 = Take.objects.create(author=clara, content='Painting is so relaxing!', reply_to=gpt_hansTake2, is_public=False)  # Clara and Hans are not friends, but this is allowed because Hans' take is public
        gpt_davidTake2 = Take.objects.create(author=david, content='I couldn’t agree more, Max!', reply_to=gpt_maxTake2, is_public=False)  # Max and David are friends
        gpt_emmaTake2 = Take.objects.create(author=emma, content='Gardening is so therapeutic', reply_to=gpt_janeTake2)
        gpt_frankTake2 = Take.objects.create(author=frank, content='Baking is an art form, John!', reply_to=gpt_johnTake2, is_public=False)  # Frank and John are not friends, but this is allowed because John's take is public
        gpt_graceTake2 = Take.objects.create(author=grace, content='Traveling opens the mind', reply_to=gpt_aliceTake2)

        # Second level replies
        gpt_henryTake2 = Take.objects.create(author=henry, content='Indeed, nature is so peaceful', reply_to=gpt_bobTake2)
        gpt_ireneTake2 = Take.objects.create(author=irene, content='I love the colors in paintings', reply_to=gpt_claraTake2, is_public=False)  # Irene and Clara are friends
        gpt_peterTake3 = Take.objects.create(author=peter, content='Music is the language of emotions', reply_to=gpt_davidTake2, is_public=False)  # Peter and David are not friends, but Max's take is public
        gpt_hansTake3 = Take.objects.create(author=hans, content='Therapeutic indeed!', reply_to=gpt_emmaTake2)
        gpt_maxTake3 = Take.objects.create(author=max, content='Baking is a skill to master', reply_to=gpt_frankTake2, is_public=False)  # Max and Frank are not friends, but John's take is public
        gpt_janeTake3 = Take.objects.create(author=jane, content='Traveling broadens horizons', reply_to=gpt_graceTake2)

        # Third level replies
        gpt_johnTake3 = Take.objects.create(author=john, content='Nature teaches us a lot', reply_to=gpt_henryTake2)
        gpt_aliceTake3 = Take.objects.create(author=alice, content='The detail in paintings is mesmerizing', reply_to=gpt_ireneTake2, is_public=False)  # Alice and Irene are not friends, but Clara's take is public
        gpt_bobTake3 = Take.objects.create(author=bob, content='Emotions are truly conveyed through music', reply_to=gpt_peterTake3, is_public=False)  # Bob and Peter are friends
        gpt_claraTake3 = Take.objects.create(author=clara, content='Gardening brings peace to the mind', reply_to=gpt_hansTake3)
        gpt_davidTake3 = Take.objects.create(author=david, content='Mastery in baking comes with practice', reply_to=gpt_maxTake3, is_public=False)  # David and Max are friends
        gpt_emmaTake3 = Take.objects.create(author=emma, content='Traveling is the best teacher', reply_to=gpt_janeTake3)

        # Fourth level replies
        gpt_frankTake3 = Take.objects.create(author=frank, content='Nature’s wisdom is endless', reply_to=gpt_johnTake3)
        gpt_graceTake3 = Take.objects.create(author=grace, content='Artistry in paintings is profound', reply_to=gpt_aliceTake3, is_public=False)  # Grace and Alice are friends
        gpt_henryTake3 = Take.objects.create(author=henry, content='Music evokes deep emotions', reply_to=gpt_bobTake3, is_public=False)  # Henry and Bob are friends
        gpt_ireneTake3 = Take.objects.create(author=irene, content='Gardening heals the soul', reply_to=gpt_claraTake3)
        gpt_peterTake4 = Take.objects.create(author=peter, content='Baking is a labor of love', reply_to=gpt_davidTake3, is_public=False)  # Peter and David are not friends, but Max's take is public
        gpt_hansTake4 = Take.objects.create(author=hans, content='Traveling enriches life', reply_to=gpt_emmaTake3)

        # Additional Takes and Replies
        gpt_maxTake4 = Take.objects.create(author=max, content='Nature photography is my hobby', reply_to=None)
        gpt_janeTake4 = Take.objects.create(author=jane, content='I enjoy crafting', reply_to=None)
        gpt_johnTake4 = Take.objects.create(author=john, content='Yoga is rejuvenating', reply_to=None, is_public=False)
        gpt_aliceTake4 = Take.objects.create(author=alice, content='I love bird watching', reply_to=None)

        gpt_bobTake4 = Take.objects.create(author=bob, content='Photography captures nature’s beauty', reply_to=gpt_maxTake4)
        gpt_claraTake4 = Take.objects.create(author=clara, content='Crafting is so fulfilling', reply_to=gpt_janeTake4)
        gpt_davidTake4 = Take.objects.create(author=david, content='Yoga brings inner peace', reply_to=gpt_johnTake4, is_public=False)  # David and John are friends
        gpt_emmaTake4 = Take.objects.create(author=emma, content='Bird watching is so relaxing', reply_to=gpt_aliceTake4)

        # Adding some variety in levels of replies
        gpt_frankTake4 = Take.objects.create(author=frank, content='Nature photography is inspiring, Max!', reply_to=gpt_bobTake4)
        gpt_graceTake4 = Take.objects.create(author=grace, content='Crafting is a great skill, Jane!', reply_to=gpt_claraTake4)
        gpt_henryTake4 = Take.objects.create(author=henry, content='Yoga has many benefits, John!', reply_to=gpt_davidTake4, is_public=False)  # Henry and David are friends
        gpt_ireneTake4 = Take.objects.create(author=irene, content='Bird watching teaches patience, Alice!', reply_to=gpt_emmaTake4)

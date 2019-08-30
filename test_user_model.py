"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


from app import app
import os
from unittest import TestCase
from flask_bcrypt import Bcrypt
from models import db, User, Message, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

bcrypt = Bcrypt()
password = 'test'
hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')


# Now we can import app


# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)

    def test_repr_model(self):
        """Testing repr return"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()
        self.assertIn("test@test.com", u.__repr__())

    def test_is_following(self):
        """Tests if one user is following another"""

        u1 = User(
            email="test@test1.com",
            username="testuser1",
            password="HASHED_PASSWORD"
        )

        u2 = User(
            email="test@test2.com",
            username="testuser2",
            password="HASHED_PASSWORD"
        )
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        follows = Follows(
            user_being_followed_id=u1.id,
            user_following_id=u2.id
        )

        db.session.add(follows)
        db.session.commit()

        self.assertTrue(u2.is_following(u1))

    def test_is_not_following(self):
        """Tests if user is not following another user"""

        u1 = User(
            email="test@test1.com",
            username="testuser1",
            password="HASHED_PASSWORD"
        )

        u2 = User(
            email="test@test2.com",
            username="testuser2",
            password="HASHED_PASSWORD"
        )
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        self.assertFalse(u2.is_following(u1))

    def test_is_followed_by(self):
        """Tests that the one user is followed by another"""

        u1 = User(
            email="test@test1.com",
            username="testuser1",
            password="HASHED_PASSWORD"
        )

        u2 = User(
            email="test@test2.com",
            username="testuser2",
            password="HASHED_PASSWORD"
        )
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        follows = Follows(
            user_being_followed_id=u1.id,
            user_following_id=u2.id
        )
        db.session.add(follows)
        db.session.commit()

        self.assertTrue(u1.is_followed_by(u2))

    def test_is_not_followed_by(self):
        """Tests that one user is not followed by the other"""

        u1 = User(
            email="test@test1.com",
            username="testuser1",
            password="HASHED_PASSWORD"
        )

        u2 = User(
            email="test@test2.com",
            username="testuser2",
            password="HASHED_PASSWORD"
        )
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        follows = Follows(
            user_being_followed_id=u2.id,
            user_following_id=u1.id
        )
        db.session.add(follows)
        db.session.commit()

        self.assertFalse(u1.is_followed_by(u2))

    def test_user_signup_successfully_creates_user(self):
        """Tests that the class method 'signup' successfully creates a new instance
        of the user class."""

        User.signup('TestyMan', 'test@test.com', 'testing',
                    'https://www.thewrap.com/wp-content/uploads/2018/09/Maniac-3.jpg')
        db.session.commit()

        successful_user = User.query.filter(
            User.username == 'TestyMan').first()

        self.assertIsInstance(successful_user, User)

    def test_user_signup_fails_on_invalid_critera(self):
        """Tests that the class method 'signup' successfully creates a new instance
        of the user class."""

        with self.assertRaises(TypeError):
            User.signup('TestyMcTesterson')

    def test_authenticates_successfuly(self):
        """Tests that the User.authenticate method successfully authenticates a user."""

        User.signup('TestyMan', 'test@test.com', 'testing',
                    'https://www.thewrap.com/wp-content/uploads/2018/09/Maniac-3.jpg')

        db.session.commit()

        self.assertTrue(User.authenticate("TestyMan", "testing"))

    def test_does_not_authenticate_invalid_user(self):
        """Tests that the User.authenticate method successfully authenticates a user."""

        User.signup('TestyMan', 'test@test.com', 'testing',
                    'https://www.thewrap.com/wp-content/uploads/2018/09/Maniac-3.jpg')

        db.session.commit()

        self.assertFalse(User.authenticate("TestyMan", "tessst"))

"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


from app import app
import os
from unittest import TestCase
from models import db, User, Message

# BEFORE we im


# Now we can import app


# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class MessageModelTestCase(TestCase):
    """Test model for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()

        self.client = app.test_client()

        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=None)
        db.session.commit()

    def test_authenticated_user_can_create_msg(self):
        """Test's that only signed in users can create messages."""

        message = Message(text='This is a test message.')
        self.testuser.messages.append(message)
        db.session.commit()

        self.assertTrue('This is a test message' in self.testuser.messages[0].text)

    def test_unauthenticated_user_can_not_create_msg(self):
        """Tests that a user who has not signed up cannot create a message."""

        u1 = User(
            email="test@test1.com",
            username="testuser1",
            password="HASHED_PASSWORD"
        )

        message = Message(text='This is a test message.')
        u1.messages.append(message)
        db.session.commit()
        
        false_user = User.query.filter(User.username == 'testuser1').first()

        with self.assertRaises(AttributeError):
            'This is a test message' in false_user.messages[0].text

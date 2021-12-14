import enum
import uuid

from rtp_backend import db


class UserTypeEnum(enum.Enum):
    admin = "Admin"
    user = "User"

class User(db.Model):
    user_id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    first_name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=False, nullable=True)
    password_hash = db.Column(db.String(100), unique=False, nullable=False)
    user_type = db.Column(
        db.Enum(UserTypeEnum), default=UserTypeEnum.user, nullable=False
    )

    def __repr__(self) -> str:
        return f"<{self.user_type}: {self.first_name} {self.last_name}>"

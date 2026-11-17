from sqlalchemy import String,DateTime
from datetime import datetime,timezone
from sqlalchemy.orm import Mapped,mapped_column
from database import Base


class User(Base):
    __tablename__="users"

    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    full_name:Mapped[str]=mapped_column(String(200),nullable=False)
    email:Mapped[str]=mapped_column(String(255),unique=True,index=True,nullable=False)
    hash_password:Mapped[str]=mapped_column(String(500),nullable=False)
    created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.now(timezone.utc))
    updated_at:Mapped[datetime]=mapped_column(DateTime,onupdate=datetime.now(timezone.utc))
    
from sqlalchemy import String, Numeric, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase):
    pass


class Investment(Base):
    __tablename__ = "investment"
    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(6, 2))

    def __repr__(self):
        return f"<Investment coin: {self.coin}, currency: {self.currency}, amount: {self.amount}>"

if __name__ == "__main__":
    engine = create_engine("sqlite:///demo.db")
    Base.metadata.create_all(engine)
    
    bitcoin = Investment(coin="bitcoin", currency="USD", amount=1.0)
    ethereum = Investment(coin="ethereum", currency="GBP", amount=10.0)
    dogecoin = Investment(coin="dogecoin", currency="INR", amount=100.0)
    
    with Session(engine) as session:
        # session.add(bitcoin)
        # session.add_all([ethereum, dogecoin])
        
        # session.commit()
        stmt = select(Investment).where(Investment.coin == "dogecoin")
        print(stmt)
        inv = session.execute(stmt).scalar_one_or_none()
        print(inv)
        inv = session.get(Investment, 1)
        print(inv)
        stmt = select(Investment).where(Investment.amount > 1)
        inv = session.execute(stmt).scalars().all()
        print([i for i in inv])
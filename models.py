import sqlalchemy


Utilisateurs = sqlalchemy.Table(
    "users",
    sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column(sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column(sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column(sqlalchemy.String,  default=('Membre')),
    sqlalchemy.Column(sqlalchemy.String, default=('Avatar/base.png'))
)



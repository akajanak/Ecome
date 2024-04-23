from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    is_active = db.Column(db.String(1))
    
    def __repr__(self) -> str:
        return f'<Post {self.name}>'
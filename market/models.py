from market import db
class User(db.Model):
      user_id = db.Column(db.Integer(),primary_key = True)
      username = db.Column(db.String(length=12),nullable = False,unique = True) 
      email = db.Column(db.String(length=20),nullable = False,unique = True)
      password_hash = db.Column(db.String(length=60),nullable = False) # flask limits hashed password to have max 60 characters
      budget = db.Column(db.Integer(),nullable =False,default = 2000)
      items = db.relationship('Item',backref = 'owned_user',lazy = True)
class Item(db.Model):
      item_id = db.Column(db.Integer(),primary_key = True)
      name = db.Column(db.String(length=30),nullable=False) # name <= 30 characters & not null
      price = db.Column(db.Integer(),nullable=False)
      barcode = db.Column(db.String(length=12),nullable = False,unique = True)
      description = db.Column(db.String(length=100),nullable=False)
      owner = db.Column(db.Integer(),db.ForeignKey('user.user_id'))
      def __repr__(self):
            return f'Item name: {self.name}'

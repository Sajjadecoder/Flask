from market import db
class Item(db.Model):
      item_id = db.Column(db.Integer(),primary_key = True)
      name = db.Column(db.String(length=30),nullable=False) # name <= 30 characters & not null
      price = db.Column(db.Integer(),nullable=False)
      barcode = db.Column(db.String(length=12),nullable = False,unique = True)
      description = db.Column(db.String(length=100),nullable=False)
      def __repr__(self):
            return f'Item name: {self.name}'

from db import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(100), unique=True)
    price = db.Column(db.Float(precision=2))
    image = db.Column(db.String)

    store = db.relationship("Store")
    storeId = db.Column(db.Integer, db.ForeignKey("stores.id"))
    isInStock = db.Column(db.Boolean, unique=False, default=True)
    reviews = db.relationship("Review", lazy="dynamic")

    def __init__(self, productName, price, image, storeId, isInStock):
        self.productName = productName
        self.price = price
        self.image = image
        self.storeId = storeId
        self.isInStock = isInStock

    def json(self):
        return {
            "id": self.id,
            "image": self.image,
            "productName": self.productName,
            "price": self.price,
            "storeId": self.storeId,
            "isInStock": self.isInStock,
            "reviews": [review.json() for review in self.reviews.all()]
        }
    
    @classmethod
    def findById(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def findByProductName(cls, productName):
        return cls.query.filter_by(productName=productName).first()

    @classmethod
    def findByStoreId(cls, _id):
        return cls.query.filter_by(storeId=_id)

    @classmethod
    def findAll(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

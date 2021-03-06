from main import db
from sqlalchemy import func

class Inventory(db.Model):
    __tablename__ = 'inventories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable= False, unique = True)
    itype = db.Column(db.String, nullable= False)
    bp = db.Column(db.Float, nullable=False)
    sp = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    stock = db.relationship('Stock', backref='inventories', lazy=True)
    sales = db.relationship('Sales', backref='inventories', lazy=True)
    
# Create
    def create_record(self):
        db.session.add(self)
        db.session.commit()
        return self


# Get Inventories
    @classmethod
    def fetch_all(cls):
        return cls.query.all()

# get_inventory_byID
    @classmethod
    def get_inventory_byID(cls, id:int):
        return cls.query.filter_by(id=id).first()
        

#Check if inventory name exists
    @classmethod
    def check_inventory_exists(cls, inventory_name:str):
        record = cls.query.filter_by(name=inventory_name).first()
        if record:
            return True
        else:
            return False


    @classmethod
    def edit_inventory(cls, inv_id, name, itype, bp, sp ):
        record = cls.query.filter_by(id=inv_id).first()
        if record:
            record.name = name
            record.itype = itype
            record.bp = bp
            record.sp =sp
            db.session.commit()
            return record
        return record

@classmethod
def delete_inventory(cls, inv_id):
    get_inventory= request.form.get(id)
    get_inventoryId= request.form.get(inv_id=inventoryId)
    inventory = Inventory.query.filter_by(id=inv_id, inv_id=inventoryId).first()
    if request.method == 'POST':
        if inventory:
            db.session.delete(inventory)
            db.session.commit()
            flash('Inventory successfully Deleted!', 'danger')

        
    return redirect(url_for('inventories'))



 

    

    

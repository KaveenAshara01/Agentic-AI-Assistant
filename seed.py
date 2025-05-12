# from app import app, db
# from app.models import Service

# sample_services = ['internet', 'hardware', 'software', 'printer', 'it']

# with app.app_context():
#     for name in sample_services:
#         # Only add if not already exists
#         if not Service.query.filter_by(name=name).first():
#             db.session.add(Service(name=name))
#     db.session.commit()
#     print("Sample services added.")


from app import app, db
from app.models import Service

with app.app_context():
    services = Service.query.all()
    if services:
        print("Available Services:")
        for service in services:
            print(f"- {service.name}")
    else:
        print("No services found.")


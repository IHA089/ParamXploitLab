from app.extensions import db
from app.models import BaseModel, ExteriorColor, Wheel, Interior, Car

def seed_data():
    if BaseModel.query.first():
        return

    print("--- Seeding database with initial data... ---")
    
    m340i = BaseModel(name='3 Series (340i)', base_price=15040000, image_file='series3.jpeg')
    ix = BaseModel(name='iX Electric', base_price=17839000, image_file='ix.jpeg')
    x5 = BaseModel(name='X5', base_price=15913000, image_file='x5.jpeg')
    db.session.add_all([m340i, ix, x5])
    
    c1 = ExteriorColor(name='Alpine White', price=0, base_model=m340i, image_file='Alpine-White.jpeg')
    c2 = ExteriorColor(name='Black Sapphire', price=1265000, base_model=m340i, image_file='Black-Sapphire.jpeg')
    c3 = ExteriorColor(name='Portimao Blue', price=1265000, base_model=m340i, image_file='Portimao-Blue.jpeg')
    w1 = Wheel(name='18" V-Spoke (Standard)', price=0, base_model=m340i, image_file='18-v.jpeg')
    w2 = Wheel(name='19" M Double-Spoke', price=1480000, base_model=m340i, image_file='19-m.jpeg')
    i1 = Interior(name='Black SensaTec (Standard)', price=0, base_model=m340i, image_file='Black-SensaTec.jpeg')
    i2 = Interior(name='Cognac SensaTec', price=0, base_model=m340i, image_file='Cognac-SensaTec.jpeg')
    i3 = Interior(name='Black Vernasca Leather', price=1350000, base_model=m340i, image_file='Black-Vernasca-Leather.jpeg')
    db.session.add_all([c1, c2, c3, w1, w2, i1, i2, i3])
    
    ix_c1 = ExteriorColor(name='Alpine White', price=1620000, base_model=ix, image_file='Alpine-White-ix.jpeg')
    ix_c2 = ExteriorColor(name='Black Sapphire', price=3600000, base_model=ix, image_file='Black-Sapphire-ix.jpeg')
    ix_c3 = ExteriorColor(name='Portimao Blue', price=4500000, base_model=ix, image_file='Portimao-Blue-ix.jpeg')
    ix_w1 = Wheel(name='20" Aero Wheels', price=0, base_model=ix, image_file='20-a.jpeg')
    ix_w2 = Wheel(name='21" Aero Wheels', price=1370000, base_model=ix, image_file='21-a.jpeg')
    ix_i1 = Interior(name='Black SensaTec', price=0, base_model=ix, image_file='Black-SensaTec.jpeg')
    ix_i2 = Interior(name='Cognac SensaTec', price=810000, base_model=ix, image_file='Cognac-SensaTec.jpeg')
    ix_i3 = Interior(name='Black Vernasca Leather', price=1810000, base_model=ix, image_file='Black-Vernasca-Leather.jpeg')
    db.session.add_all([ix_c1, ix_c2, ix_c3, ix_w1, ix_w2, ix_i1, ix_i2, ix_i3])

    x5_c1 = ExteriorColor(name='Alpine White', price=1820000, base_model=x5, image_file='Alpine-White-x5.jpeg')
    x5_c2 = ExteriorColor(name='Black Sapphire', price=2020000, base_model=x5, image_file='Black-Sapphire-x5.jpeg')
    x5_c3 = ExteriorColor(name='Portimao Blue', price=2150000, base_model=x5, image_file='Portimao-Blue-x5.jpeg')
    x5_w1 = Wheel(name='21" Y-Spoke', price=1370000, base_model=x5, image_file='21-y.jpeg')
    x5_w2 = Wheel(name='22" Y-Spoke', price=1370000, base_model=x5, image_file='22-y.jpeg')
    x5_i1 = Interior(name='Black SensaTec', price=0, base_model=x5, image_file='Black-SensaTec.jpeg')
    x5_i2 = Interior(name='Cognac SensaTec', price=0, base_model=x5, image_file='Cognac-SensaTec.jpeg')
    x5_i3 = Interior(name='Black Vernasca Leather', price=0, base_model=x5, image_file='Black-Vernasca-Leather.jpeg')
    db.session.add_all([x5_c1, x5_c2, x5_c3, x5_w1, x5_w2, x5_i1, x5_i2, x5_i3])


    car1 = Car(model='M2 Competition', year='2024', price='₹1.03 Crore*', description='Compact, track-focused M coupe with aggressive styling, sharp handling and M-tuned chassis.', image_file='M2-Competition.jpeg', engine='3.0 L inline-6 twin-turbo (M TwinPower Turbo)', zero_to_sixty='~4.0', range='N/A', transmission='8-speed M Steptronic / 6-speed manual', color='Brooklyn Grey / Skyscraper Grey / Dragon Fire Red')
    car2 = Car(model='M3 (G80)', year='2024', price='~₹1.47 Crore*', description='High-performance sports sedan blending daily usability with race-bred M performance and strong midrange torque.', image_file='M3.jpeg', engine='3.0 L inline-6 twin-turbo (M TwinPower Turbo)', zero_to_sixty='~3.8–4.2', range='N/A', transmission='6-speed manual or 8-speed M automatic', color='Brooklyn Grey / Alpine White / Isle of Man Green')
    car3 = Car(model='M4 Competition', year='2024', price='₹1.52 Crore*', description='Coupe/Gran Coupe M4 Competition — raw performance with lightweight components, M xDrive option and track capability.', image_file='M4-Competition.jpeg', engine='3.0 L inline-6 twin-turbo (M TwinPower Turbo)', zero_to_sixty='~3.2–3.5', range='N/A', transmission='8-speed M Steptronic automatic', color='Brooklyn Grey / Portimao Blue / Toronto Red')
    car4 = Car(model='M5 Competition', year='2024', price='₹2.01 Crore*', description='Executive super-sedan with a thundering twin-turbo V8, AWD (xDrive) on Competition, and lavish interior tech.', image_file='M5-Competition.jpeg', engine='4.4 L V8 twin-turbo + electric assist on latest PHEV variants (mix varies by model)', zero_to_sixty='~3.1–3.3', range='N/A (fuel)', transmission='8-speed M Steptronic automatic', color='M Brooklyn Grey / Black Sapphire / Marina Bay Blue')
    car5 = Car(model='M6 Gran Coupé', year='2015', price='~₹1.71–1.85 Crore*', description='Grand-touring 4-door coupe with V8 muscle and refined luxury — a blend of comfort and performance.', image_file='M6-Gran-Coupe.jpeg', engine='4.4 L V8 twin-turbo', zero_to_sixty='~4.2', range='N/A', transmission='7-speed M double-clutch automatic', color='Jatoba Metallic / Singapore Grey / Black Sapphire')
    car6 = Car(model='M8 Competition', year='2024', price='₹2.38 Crore*', description='Flagship performance coupe/gran coupe combining 600+ hp V8, carbon-fibre trim and ultra-refined cabin.', image_file='M8-Competition.jpeg', engine='4.4 L V8 twin-turbo (M TwinPower Turbo)', zero_to_sixty='~3.0–3.2', range='N/A', transmission='8-speed M Steptronic with Drivelogic', color='Brooklyn Grey / Aventurine Red / Man Green Metallic')
    car7 = Car(model='i8', year='2019–2020', price='~₹2.14–2.62 Crore*', description='Plug-in hybrid sports car — futuristic styling, scissor doors and a petrol + electric hybrid powertrain.', image_file='i8.jpeg', engine='1.5 L inline-3 petrol + electric motor (plug-in hybrid)', zero_to_sixty='~4.2–4.4', range='Electric range: ~15–37 miles', transmission='6-speed automatic (hybrid coupling)', color='Crystal White / Protonic Blue / Sophisto Grey')
    car8 = Car(model='X6 M Competition', year='2025/2026', price='~₹1.82 Crore*', description='Coupe-style SUV with brutal V8 power, sporty handling and luxury SUV comfort.', image_file='X6-M-Competition.jpeg', engine='4.4 L V8 twin-turbo (M TwinPower Turbo) with 48V mild-hybrid on latest specs', zero_to_sixty='~3.7–3.9', range='N/A', transmission='8-speed automatic (M Steptronic)', color='Carbon Black / Mineral White / Marina Bay Blue')
    car9 = Car(model='Z4 M40i', year='2024/2025', price='₹87.9–96.9 Lakh*', description='Two-seat roadster with a free-revving inline-6, open-top dynamics and pure driving feel.', image_file='Z4-M40i.jpeg', engine='3.0 L inline-6 turbo (B58 family)', zero_to_sixty='~4.5', range='N/A', transmission='8-speed Steptronic Sport automatic', color='Alpine White / Skyscraper Grey / Portimao Blue / Thundernight')
    car10 = Car(model='i7 (BMW 7 Series EV)', year='2024/2025', price='₹2.05–2.58 Crore*', description='Flagship fully-electric 7-Series limousine combining opulent luxury and long EV range with advanced onboard tech.', image_file='i7.jpeg', engine='Electric (dual-motor eDrive variants) — power varies by trim', zero_to_sixty='~4.7', range='~320–388 miles', transmission='Single-speed reduction gear (EV)', color='Sophisto Grey / Black Sapphire / Mineral White')
    car11 = Car(model='X5 M Competition', year='2024/2025', price='~₹2.08 Crore*', description='Performance SUV with M-tuned chassis, V8 grunt and family-usable interior tech.', image_file='X5-M-Competition.jpeg', engine='4.4 L V8 twin-turbo (M TwinPower Turbo)', zero_to_sixty='~3.8–4.0', range='N/A', transmission='8-speed automatic (M Steptronic)', color='Carbon Black / Toronto Red / Marina Bay Blue')
    car12 = Car(model='X3 M Competition', year='2024', price='~₹99.9 Lakh*', description='Compact performance SUV with the M3/M4 inline-6 tuned for SUV use — punches well above its weight.', image_file='X3-M-Competition.jpeg', engine='3.0 L inline-6 twin-turbo', zero_to_sixty='~3.8–4.1', range='N/A', transmission='8-speed automatic', color='Black Sapphire / Alpine White / Portimao Blue')
    db.session.add_all([car1, car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, car12])

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"--- Error seeding database: {e} ---")
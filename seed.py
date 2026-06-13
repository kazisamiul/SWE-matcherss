import sys
from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app import models, crud, schemas

def seed_database():
    print("Recreating database tables...")
    # Drop and recreate tables to ensure a clean slate
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    db: Session = SessionLocal()
    try:
        print("Inserting master lists...")
        # 1. Master Languages
        languages = ["Python", "Java", "C++", "JavaScript", "Go", "Rust", "TypeScript"]
        for name in languages:
            crud.get_or_create_language(db, name)
            
        # 2. Master DSA Topics
        dsa_topics = ["Arrays", "Linked Lists", "Trees", "Graphs", "Dynamic Programming", "Sorting & Searching", "Recursion"]
        for name in dsa_topics:
            crud.get_or_create_dsa_topic(db, name)
            
        print("Creating sample users (Software Engineers)...")
        # 3. Add Users
        users_data = [
            schemas.UserCreate(
                name="Alice Vance",
                email="alice@google.com",
                bio="Backend Developer specializing in Python/Go, passionate about optimization and Dynamic Programming.",
                languages=["Python", "Go", "TypeScript"],
                dsa_skills=[
                    schemas.UserDSASkillCreate(dsa_topic_name="Arrays", proficiency=5),
                    schemas.UserDSASkillCreate(dsa_topic_name="Dynamic Programming", proficiency=4),
                    schemas.UserDSASkillCreate(dsa_topic_name="Recursion", proficiency=4)
                ]
            ),
            schemas.UserCreate(
                name="Bob Miller",
                email="bob@netflix.com",
                bio="Systems Engineer. Expert in C++ and low-level optimizations. Strong understanding of Graphs and Trees.",
                languages=["C++", "Java", "Rust"],
                dsa_skills=[
                    schemas.UserDSASkillCreate(dsa_topic_name="Graphs", proficiency=5),
                    schemas.UserDSASkillCreate(dsa_topic_name="Trees", proficiency=4),
                    schemas.UserDSASkillCreate(dsa_topic_name="Sorting & Searching", proficiency=4)
                ]
            ),
            schemas.UserCreate(
                name="Charlie Kim",
                email="charlie@stripe.com",
                bio="Frontend/Full Stack engineer with a focus on UI responsiveness and algorithms.",
                languages=["JavaScript", "TypeScript", "Python"],
                dsa_skills=[
                    schemas.UserDSASkillCreate(dsa_topic_name="Arrays", proficiency=4),
                    schemas.UserDSASkillCreate(dsa_topic_name="Linked Lists", proficiency=3),
                    schemas.UserDSASkillCreate(dsa_topic_name="Trees", proficiency=2)
                ]
            )
        ]
        
        for u_data in users_data:
            crud.create_user(db, u_data)
            print(f"  Created user: {u_data.name}")
            
        print("Creating sample job postings (Recruiters)...")
        # 4. Add Jobs
        jobs_data = [
            schemas.JobCreate(
                title="Senior Python Backend Engineer",
                description="We are looking for a Senior Developer to build scaling cloud systems. Dynamic programming knowledge is key for our optimization engines.",
                company="Pycorp Inc.",
                location="Remote",
                salary="$130k - $160k",
                languages=["Python", "Go"],
                dsa_requirements=[
                    schemas.JobDSARequirementCreate(dsa_topic_name="Dynamic Programming", min_proficiency=3),
                    schemas.JobDSARequirementCreate(dsa_topic_name="Arrays", min_proficiency=4)
                ]
            ),
            schemas.JobCreate(
                title="Core Database Engine Engineer",
                description="Build next-gen key-value storage. High concurrency, distributed graphs, and tree indexing structures.",
                company="DbTech Labs",
                location="San Francisco, CA",
                salary="$180k - $220k",
                languages=["C++", "Rust"],
                dsa_requirements=[
                    schemas.JobDSARequirementCreate(dsa_topic_name="Graphs", min_proficiency=4),
                    schemas.JobDSARequirementCreate(dsa_topic_name="Trees", min_proficiency=5),
                    schemas.JobDSARequirementCreate(dsa_topic_name="Sorting & Searching", min_proficiency=4)
                ]
            ),
            schemas.JobCreate(
                title="Frontend Engineer (React)",
                description="Create beautiful responsive user interfaces. Must be comfortable with JavaScript/TypeScript and tree traversal algorithms.",
                company="DesignFlow",
                location="New York, NY",
                salary="$110k - $140k",
                languages=["JavaScript", "TypeScript"],
                dsa_requirements=[
                    schemas.JobDSARequirementCreate(dsa_topic_name="Arrays", min_proficiency=3),
                    schemas.JobDSARequirementCreate(dsa_topic_name="Trees", min_proficiency=2)
                ]
            ),
            schemas.JobCreate(
                title="Full Stack Engineer",
                description="Help us build SaaS portals. Proficiency in Python web servers and Frontend typescript is required.",
                company="SaaSify",
                location="Hybrid (Austin, TX)",
                salary="$120k - $150k",
                languages=["Python", "JavaScript", "TypeScript"],
                dsa_requirements=[
                    schemas.JobDSARequirementCreate(dsa_topic_name="Arrays", min_proficiency=3),
                    schemas.JobDSARequirementCreate(dsa_topic_name="Linked Lists", min_proficiency=3)
                ]
            )
        ]
        
        for j_data in jobs_data:
            crud.create_job(db, j_data)
            print(f"  Created job: {j_data.title} at {j_data.company}")
            
        print("Database seeding completed successfully!")
    except Exception as e:
        print(f"Error seeding database: {e}")
        sys.exit(1)
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()

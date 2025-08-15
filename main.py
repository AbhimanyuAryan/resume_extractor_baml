import asyncio
from baml_client import b
from baml_client.types import Resume

def main():
    resume_info = b.ExtractResume("Resume of steve jobs")
    print(resume_info)
    assert isinstance(resume_info, Resume)
    print(f"Name: {resume_info.name}")
    print(f"Email: {resume_info.email}")
    print(f"Experience: {resume_info.experience}")
    print(f"Skills: {resume_info.skills}")

if __name__ == '__main__':
    main()

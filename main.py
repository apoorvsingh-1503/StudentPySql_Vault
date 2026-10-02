from Admin import Admin
from Student import Student

def main():
        while True:
            print(f"=== WELCOME TO APOORV STUDENT SYSTEM ===")
            print("1. ADMIN LOGIN")
            print("2. STUDENT LOGIN")
            choice = input("Select option (1/2 or 'q' to quit): ").lower()

            if choice == '1':
                Admin.main1()
            elif choice == '2':
                Student.main2()
            elif choice == 'q':
                break

if __name__ == "__main__":
    main() 

from nazarii_bryniarskyi.structure.service.StudentService import StudentService

if __name__ == '__main__':
    service = StudentService()
    service.print_all_students()
    losers = service.find_losers()

    print("\nLosers:")

    for i, loser in enumerate(losers, start=1):
        print(f"{i}. {loser}")

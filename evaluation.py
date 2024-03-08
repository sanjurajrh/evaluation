def ask_question(question):
    print(question)
    answer = input("Your answer: ")
    return answer.strip()

def main():
    predefined_questions = [
        "What is your name? ",
        "What is the name of the module you have attended? ",
        "_______ maintain maps of the cluster state. ",
        "_______ store data and handle data replication, recovery and rebalancing ",
        "_______ keep track of runtime metrics and expose cluster information through a browser-based dashboard and REST API ",
        "_______ store metadata used by CephFS to allow efficient POSIX command execution by clients. ",
        "What is the object storage backend known as _______? ",
        "What are the building blocks of a Ceph Storage cluster? ",
        "Ceph uses ________ algorithm to efficiently compute information about object location, instead of having to depend on a central lookup table. ",
        "Each OSD has its own _______ ",
        "CRUSH assigns every object to a single hash bucket, known as a _______. ",
        "_____ represents the global namespace for all objects and buckets in the multisite replication space. "
    ]

    try:
        with open("user_answers8.txt", "w") as file:
            for question in predefined_questions:
                answer = ask_question(question)
                file.write(f"{question} | {answer}\n")
        print("User answers recorded in 'user_answers8.txt'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


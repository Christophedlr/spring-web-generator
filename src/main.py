print("Spring-web Generator V1.0")
print("Copyright (c) 2020 Christophe Daloz - De Los Rios")

configuration: dict = {}
confirmation: str = ""


def answer():
    global configuration

    print("Version of Spring Boot:")
    configuration['spring_boot'] = input()

    print("Version of Java:")
    configuration['java'] = input()

    print("Package name:")
    configuration['package_name'] = input()

    print("Name of project:")
    configuration['name'] = input()

    print("Description:")
    configuration['description'] = input()

    print("Group:")
    configuration['group'] = input()

    print("Artifact:")
    configuration['artifact'] = input()

    print("Location:")
    configuration['location'] = input()


def summary():
    global confirmation

    print("Summary")
    print("-------")
    print("Version of Spring Boot: " + configuration['spring_boot'])
    print("Version of Java: " + configuration['java'])
    print("Package name: " + configuration['package_name'])
    print("Name of project: " + configuration['name'])
    print("Description: " + configuration['description'])
    print("Group: " + configuration['group'])
    print("Artifact: " + configuration['artifact'])
    print("Location: " + configuration['location'])
    print('Confirm generation ? [Y/n]')

    confirmation = input()
    confirmation = 'y' if not confirmation else confirmation


while confirmation.lower() != 'y':
    answer()
    summary()

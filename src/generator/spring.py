import os
from zipfile import ZipFile
from pathlib import Path


# SpringBoot base code generator
class SpringBoot:
    spring_boot: str
    java_version: str
    project_version: str
    package_name: str
    name: str
    description: str
    group: str
    artifact: str
    location: str

    def __init__(self, spring_boot, java_version, project_version, package_name, name, description, group, artifact,
                 location):
        self.spring_boot = spring_boot
        self.java_version = java_version
        self.project_version = project_version
        self.package_name = package_name
        self.name = name
        self.description = description
        self.group = group
        self.artifact = artifact
        self.location = location

    # Update & generate files for project
    def generate(self):
        with ZipFile('../resources/springboot.zip', 'r') as zip:
            print("Extraction of base files")
            zip.extractall(self.location)

            print("Updating pom.xml")
            self._pom_xml_file()

            print("Generate files")
            self._gen_files()

            print("Finished generation of project")

    # Update pom.xml file
    def _pom_xml_file(self):
        fopen = open(self.location+os.sep+"pom.xml", 'rt')
        data = fopen.read()
        fopen.close()

        data = data.replace(
            '\t<groupId></groupId>\n'
            '\t<artifactId></artifactId>\n'
            '\t<version></version>\n'
            '\t<name></name>\n'
            '\t<description></description>\n',
            '\t<groupId>' + self.group + '</groupId>\n'
            '\t<artifactId>' + self.artifact + '</artifactId>\n'
            '\t<version>' + self.project_version + '</version>\n'
            '\t<name>' + self.name + '</name>\n'
            '\t<description>' + self.description + '</description>\n'
        )
        data = data.replace('<version></version>', '<version>' + self.spring_boot + '</version>')
        data = data.replace('<java.version></java.version>', '<java.version>' + self.java_version + '</java.version>')

        fopen = open(self.location+os.sep+"pom.xml", 'wt')
        fopen.write(data)
        fopen.close()

    # Generation files & resources configuration
    def _gen_files(self):
        directories = self.package_name.replace('.', os.sep)
        split = self.package_name.split('.')
        src_dir = self.location+os.sep+'src'+os.sep+'main'+os.sep+'java'+os.sep+directories
        test_dir = self.location+os.sep+'test'+os.sep+'java'+os.sep+directories
        resources_dir = self.location+os.sep+'resources'
        application = (
            "package "+self.package_name+";\n\n"
            "import org.springframework.boot.SpringApplication;\n"
            "import org.springframework.boot.autoconfigure.SpringBootApplication;\n\n"
            "@SpringBootApplication\n"
            "public class "+split[len(split)-1].capitalize()+"Application {\n"
            "    public static void main(String[] args) {\n"
            "        SpringApplication.run("+split[len(split)-1].capitalize()+"Application.class, args);\n"
            "    }\n"
            "}\n"
        )
        test = (
            "package "+self.package_name+";\n\n"
            "import org.junit.jupiter.api.Test;\n"
            "import org.springframework.boot.test.context.SpringBootTest;\n\n"
            "@SpringBootTest\n"
            "public class "+split[len(split)-1].capitalize()+"ApplicationTests {\n"
            "    @Test\n"
            "    void contextLoads() {\n"
            "    }\n"
            "}\n"
        )

        print("Create directories structure")
        path = Path(src_dir)
        path.mkdir(parents=True, exist_ok=True)

        path = Path(test_dir)
        path.mkdir(parents=True, exist_ok=True)

        path = Path(resources_dir)
        path.mkdir(parents=True, exist_ok=True)

        print("Create application class")
        fopen = open(src_dir+os.sep+split[len(split)-1].capitalize()+"Application.java", 'wt')
        fopen.write(application)
        fopen.close()

        print("Create test application class")
        fopen = open(test_dir+os.sep+split[len(split)-1].capitalize()+"ApplicationTests.java", 'wt')
        fopen.write(test)
        fopen.close()

        print("Create application properties")
        fopen = open(resources_dir+os.sep+"application.properties", 'wt')
        fopen.write(
            "spring.web.resources.static-locations=classpath:/META-INF/resources/,"
            "classpath:/META-INF/resources/webjars/"
        )
        fopen.close()

import os
import xml.etree.ElementTree as ET


class CsprojReader:

    @staticmethod
    def read(repo_path):

        output = []

        for root, _, files in os.walk(repo_path):

            for file in files:

                if not file.endswith(".csproj"):
                    continue

                path = os.path.join(root, file)

                try:

                    tree = ET.parse(path)

                    root_xml = tree.getroot()

                    framework = ""

                    packages = []

                    for elem in root_xml.iter():

                        tag = elem.tag.split("}")[-1]

                        if tag == "TargetFramework":

                            framework = elem.text

                        elif tag == "PackageReference":

                            packages.append(
                                elem.attrib.get("Include", "")
                            )

                    output.append(
                        f"{file}\n"
                        f"Framework: {framework}\n"
                        f"Packages: {', '.join(packages[:10])}"
                    )

                except:
                    pass

        return "\n\n".join(output)
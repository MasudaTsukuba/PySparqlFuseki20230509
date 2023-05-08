import subprocess


def convert_csv_to_rdf(csv_file):
    cp = subprocess.run(
        ['java', '-jar', '../rmlmapper/rmlmapper-6.1.3-r367-all.jar', '-m',
         f'rml/rml_{csv_file}.ttl', '-o', f'../rml_rdf/{csv_file}_rdf.ttl', '-s', 'turtle'])
    if cp.returncode != 0:
        print('Error: rmlmapper')
        return -1
    pass


if __name__ == '__main__':
    # convert_csv_to_rdf('hotel')
    # convert_csv_to_rdf('museum')
    # convert_csv_to_rdf('building')
    # convert_csv_to_rdf('heritage')
    # convert_csv_to_rdf('hotel_country')
    # convert_csv_to_rdf('museum_country')
    convert_csv_to_rdf('building_country')
    # convert_csv_to_rdf('heritage_country')
    # convert_csv_to_rdf('hotel_place')
    # convert_csv_to_rdf('museum_place')
    # convert_csv_to_rdf('building_place')
    # convert_csv_to_rdf('heritage_place')

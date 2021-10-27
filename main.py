import pandas as pd


def parse_data():
    return {
        'hostname': str,
        'ansible_port': str,
        'ansible_host': str,
        'ansible_user': str,
        'ansible_password': str,
        'ansible_connection': str,
    }


def write_inventory(server_list, f):
    for server in server_list[2:]:
        f.write(server[0] + " ")
        for idx in range(1, len(server)):
            f.write(server_list[0][idx] + "=" + server[idx] + " ")
        f.write('\n')


if __name__ == '__main__':
    filename = "file.xlsx"
    server_frame = pd.read_excel(filename, dtype=parse_data(), header=None, sheet_name="작업대상서버",
                                na_values="N/A")
    server_list = server_frame.values.tolist()

    with open("test_result", "w") as f:
        write_inventory(server_list, f)


from building import Building

def main():
    building = Building[str]()

    building.add_item("chair")
    building.add_item("table")
    building.add_item("desk")

    print(building.num_items())
    print(building.get_item(1))

    building.remove_item(0)

    print(building.num_items())


if __name__ == '__main__':
    main()
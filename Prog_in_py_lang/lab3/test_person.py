from person import Person

def test_save_and_load():
    person1 = Person(
        first_name="Anna",
        last_name="Smith",
        address="123 Main Street, London",
        postal_code="SW1A 1AA",
        national_id="95050567890"
    )

    test_file = "test_person.json"

    person1.save_to_json(test_file)

    person2 = Person.load_from_json(test_file)
    
    assert person1 == person2, "Error: Data mismatch after loading from JSON!"

    print("✅ Test passed successfully! Data matches.")

if __name__ == "__main__":
    test_save_and_load()

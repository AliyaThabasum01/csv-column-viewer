from analyzer import analyze_csv

print("📊 CSV Column Viewer")
print("=" * 35)

filename = input("Enter CSV file path: ").strip()

result = analyze_csv(filename)

if result is None:
    print("❌ File not found.")
else:
    print("\n📋 CSV Summary")
    print("=" * 35)
    print(f"Rows    : {result['rows']}")
    print(f"Columns : {result['columns']}")

    print("\nColumn Names:")
    for column in result["names"]:
        print(f"  • {column}")

    print("\nFirst 3 Rows:")
    for row in result["sample"]:
        print(row)

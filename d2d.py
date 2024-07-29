import argparse

def convert_to_bits(size, unit):
    if unit == 'GB':
        return size * 8 * 1e9  # 1 GB = 8e9 bits
    elif unit == 'TB':
        return size * 8 * 1e12  # 1 TB = 8e12 bits
    else:
        raise ValueError("Unsupported unit. Use 'GB' or 'TB'.")

def convert_to_bits_per_second(speed, unit):
    if unit == 'Gb':
        return speed * 1e9  # 1 Gb = 1e9 bits
    elif unit == 'Mb':
        return speed * 1e6  # 1 Mb = 1e6 bits
    else:
        raise ValueError("Unsupported unit. Use 'Gb' or 'Mb'.")

def calculate_transfer_time(size_bits, speed_bps):
    return size_bits / speed_bps  # Time in seconds

def main():
    parser = argparse.ArgumentParser(description="Calculate file transfer time over different network speeds.")
    parser.add_argument("size", type=float, help="Size of the data (e.g., 10)")
    parser.add_argument("size_unit", choices=['GB', 'TB'], help="Unit of the data size (GB or TB)")
    parser.add_argument("speed", type=float, help="Link speed (e.g., 1)")
    parser.add_argument("speed_unit", choices=['Gb', 'Mb'], help="Unit of the link speed (Gb or Mb)")

    args = parser.parse_args()

    size_bits = convert_to_bits(args.size, args.size_unit)
    speed_bps = convert_to_bits_per_second(args.speed, args.speed_unit)
    transfer_time_seconds = calculate_transfer_time(size_bits, speed_bps)

    hours = transfer_time_seconds // 3600
    minutes = (transfer_time_seconds % 3600) // 60
    seconds = transfer_time_seconds % 60

    print(f"Transfer time for {args.size} {args.size_unit} over a {args.speed} {args.speed_unit} link:")
    print(f"{int(hours)} hours, {int(minutes)} minutes, {seconds:.2f} seconds")

if __name__ == "__main__":
    main()
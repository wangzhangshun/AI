start_id = 5
start_km = 375.5
end_km = 445.5
step = 0.5

current_km = start_km
id_counter = start_id

print("INSERT INTO hhg_ims.station_kilometer_list (id, start_standard_kilometer, start_standard_unit_meter, stop_standard_kilometer, stop_standard_unit_meter, creator, create_time, updater, update_time, deleted, tenant_id) VALUES ")

while current_km < end_km:
    next_km = current_km + step
    # 格式化公里标字符串
    start_str = f"k{int(current_km)}+{str(int((current_km % 1) * 1000)).zfill(3)}" if current_km % 1 != 0 else f"k{int(current_km)}.000"
    end_str = f"k{int(next_km)}+{str(int((next_km % 1) * 1000)).zfill(3)}" if next_km % 1 != 0 else f"k{int(next_km)}.000"

    print(
        f"({id_counter}, {current_km:.3f}, '{start_str}', {next_km:.3f}, '{end_str}', '', '2025-07-18 22:31:27', '', '2025-07-18 22:36:22', 0, 1),")

    current_km = next_km
    id_counter += 1
import os
import time
import subprocess

COM_PORT = "/dev/cu.usbserial-EN472951"


def test_emotion_analyzer():
    test_dir = "test"
    total_time = 0
    total_files = 0
    success_count = 0
    failure_count = 0

    for filename in os.listdir(test_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(test_dir, filename)
            with open(filepath, "r") as f:
                text = f.read()
            
            print(f"--- Testing with {filename} ---")
            print(text)
            command = [
                "python3",
                "emotion_analyzer.py",
                text,
                "-c", COM_PORT
            ]
            
            start_time = time.time()
            try:
                subprocess.run(command, check=True)
                elapsed = time.time() - start_time
                total_time += elapsed
                success_count += 1
                print(f"✓ Success ({elapsed:.2f} sec)")
            except subprocess.CalledProcessError as e:
                failure_count += 1
                elapsed = time.time() - start_time
                print(f"✗ Error running emotion_analyzer.py for {filename}: {e} ({elapsed:.2f} sec)")
            total_files += 1
            print("---------------------------\n")

            time.sleep(2)

    # Summary
    print("========== Summary ==========")
    print(f"Total files tested  : {total_files}")
    print(f"Successful tests    : {success_count}")
    print(f"Failed tests        : {failure_count}")
    print(f"Total time taken    : {total_time:.2f} sec")
    if total_files > 0:
        print(f"Average time/file   : {total_time / total_files:.2f} sec")
    print("=============================")

if __name__ == "__main__":
    test_emotion_analyzer()

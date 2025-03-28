import subprocess
import time

def generate_sadtalker_video(image_path, audio_path, eyeblink_path, result_path, output_video="sadtalker_output.mp4"):
    """Generate a talking face video using SadTalker."""
    start_time = time.time()
    command = [
        "poetry", "run", "python", "SadTalker/inference.py",
        "--driven_audio", audio_path,
        "--source_image", image_path,
        # "--ref_eyeblink", eyeblink_path,  # Uncomment this line to use eye blinking from a reference video
        "--checkpoint_dir", "./SadTalker/checkpoints",
        "--result_dir", result_path,
        "--batch_size", "8",
        "--still",
        "--preprocess", "full",
        "--enhancer", "gfpgan" 
    ]
    subprocess.run(command)
    end_time = time.time()  # End time
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f"SadTalker video generation completed in {elapsed_time:.2f} seconds.")


if __name__ == "__main__":
    image = "./SadTalker/examples/source_image/happy1.png"
    audio = "./SadTalker/examples/driven_audio/fayu.wav"
    eyeblink= "./SadTalker/examples/ref_video/WDA_AlexandriaOcasioCortez_000.mp4"
    result = "./SadTalker/examples/results"
    generate_sadtalker_video(image, audio, eyeblink, result)
import { useState } from 'react'
import './App.css'

function App() {
  const [inputVideo, setInputVideo] = useState<File | null>(null);
  let videoDone: boolean = false;

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    console.log("File changed")

    if (event.target.files && event.target.files.length > 0)
      setInputVideo(event.target.files[0]);
  };

  const handleSubmit = async () => {
    console.log("Submit clicked")

    if (!inputVideo) {
      alert("Select a video first!");
      return;
    }

    const formData = new FormData();
    formData.append("video", inputVideo);

    try {
      await fetch("http://localhost:8000/burn-captions", { method: "POST", body: formData })
      videoDone = true;
    }
    catch (err) {
      console.error("Error uploading video: ", err);
    }
  }

  return (
    <>
      <div className="uploadDiv">
        <div>
          <label> Select a video to upload </label>
          <input type="file" accept="video/mp4" onChange={handleFileChange} />
        </div>
        <div>
          <button onClick={handleSubmit}>Submit</button>
        </div>
      </div>

      <div className="outputDiv">
        {videoDone &&
          <video controls>
            <source src="http://localhost:8000/temp/output.mp4" type="video/mp4" />
          </video>
        }
      </div>
    </>
  )
}

export default App

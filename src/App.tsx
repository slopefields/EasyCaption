import { useState } from 'react'
import './App.css'

function App() {
  const [inputVideo, setInputVideo] = useState<File | null>(null);
  const [translate, setTranslate] = useState<boolean>(false);
  const [videoDone, setVideoDone] = useState<boolean>(false);
  const [videoKey, setVideoKey] = useState<number>(0);


  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    console.log("File changed")

    if (event.target.files && event.target.files.length > 0)
      setInputVideo(event.target.files[0]);
  };

  const handleTranslateChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setTranslate(event.target.value === "translate");
  };

  const handleSubmit = async () => {
    console.log("Submit clicked")

    if (!inputVideo) {
      alert("Select a video first!");
      return;
    }

    const formData = new FormData();
    formData.append("video", inputVideo);
    formData.append("translate", translate ? "true" : "false");

    try {
      await fetch("http://localhost:8000/burn-captions", { method: "POST", body: formData });
      setVideoDone(true);
      setVideoKey(Date.now());
    }
    catch (err) {
      console.error("Error uploading video: ", err);
    }
  }

  return (
    <>
      <div className="title">
        EasyCaption
      </div>
      <div className="uploadDiv">
        <div>
          <label> Select a video to upload: </label>
          <input type="file" accept="video/mp4" onChange={handleFileChange} />
        </div>

        <div>
          <label> Translation option: </label>
          <select onChange={handleTranslateChange}>
            <option value="original">Keep original language</option>
            <option value="translate">Translate to English</option>
          </select>
        </div>

        <div>
          <button onClick={handleSubmit}>Submit</button>
        </div>
      </div>

      <div className="outputDiv">
        {videoDone &&
          <video controls key={videoKey}>
            <source src={`http://localhost:8000/temp/output.mp4?t=${videoKey}`} type="video/mp4" />
          </video>
        }
      </div>
    </>
  )
}

export default App

import { useState } from 'react'
import './App.css'

function App() {
  const [inputVideo, setInputVideo] = useState<File | null>(null);



  return (
    <>
      <div className="mainArea">
        <div>
          <label> Select a video to upload </label>
          <input type="file" accept="video/mp4" name="videoUpload" />
        </div>
        <div>
          <button>Submit</button>
        </div>
      </div>
    </>
  )
}

export default App

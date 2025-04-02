import './index.css'

function App() {

  return (
    <>
      <div className="container">
        <div className="header">
          <h1>TodoAPP</h1>
        </div>
        <div className="sideMenu">
          <h2>Minhas Listas</h2>
          <ul>
            <li>compras</li>
            <li>lembretes</li>
            <li>trabalhos facul</li>
          </ul>
          <button type="button">nova lista</button>
        </div>
        <div className="main">
          <h2>Compras</h2>
          <button type='button'>
            <h3>nova tarefa</h3>
            </button>
        </div>
      </div>
    </>
  )
}

export default App

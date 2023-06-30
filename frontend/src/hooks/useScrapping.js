import { useCallback } from 'react'


export default function useUser() {

    const scraping = useCallback((documento, contrasena, setEstado) => {
        const URL = 'http://localhost:8000/users/scarping/'

        console.log(`Entra al scraping.`)

        setEstado(2)

        fetch(
            URL,
            {
                method: 'GET'
            }
        )
            .then(response => response.json())
            .then((obj) => {

                console.log(obj)

            })
            .catch(error => {
                setEstado(-400)
                console.error(`Error: ${error}`)
            })

    }, [])

    return {
        scraping
    }
}
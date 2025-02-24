package edu.utvt.springdata;

import edu.utvt.springdata.model.Usuario;
import edu.utvt.springdata.model.Cliente;
import edu.utvt.springdata.repository.UsuarioRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

import static org.junit.jupiter.api.Assertions.*;

@DataJpaTest
public class InheritanceTests {

    @Autowired
    private UsuarioRepository usuarioRepository;

    @Test
    public void testGuardarCliente() {
        Cliente cliente = new Cliente();
        cliente.setNombre("Juan");
        cliente.setApellidos("Pérez");
        cliente.setEmail("juan@example.com");
        
        Cliente savedCliente = usuarioRepository.save(cliente);
        
        assertNotNull(savedCliente.getId());
        assertEquals("Juan", savedCliente.getNombre());
    }

    @Test
    public void testBuscarUsuarioPorId() {
        Cliente cliente = new Cliente();
        cliente.setNombre("Ana");
        cliente.setApellidos("Gómez");
        cliente.setEmail("ana@example.com");

        Cliente savedCliente = usuarioRepository.save(cliente);
        Optional<UsuarioRepository> foundUsuario = usuarioRepository.findById(savedCliente.getId());

        assertTrue(foundUsuario.isPresent());
        assertEquals("Ana", foundUsuario.get().getNombre());
    }

    @Test
    public void testBuscarTodosLosUsuarios() {
        Cliente cliente1 = new Cliente();
        cliente1.setNombre("Carlos");
        cliente1.setApellidos("López");
        cliente1.setEmail("carlos@example.com");

        Cliente cliente2 = new Cliente();
        cliente2.setNombre("María");
        cliente2.setApellidos("Fernández");
        cliente2.setEmail("maria@example.com");

        usuarioRepository.save(cliente1);
        usuarioRepository.save(cliente2);

        List<UsuarioRepository> usuarios = usuarioRepository.findAll();

        assertFalse(usuarios.isEmpty());
        assertEquals(2, usuarios.size());
    }
}

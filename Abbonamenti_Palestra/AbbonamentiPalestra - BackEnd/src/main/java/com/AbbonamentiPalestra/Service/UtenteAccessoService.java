package com.AbbonamentiPalestra.Service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.AbbonamentiPalestra.Class.UtenteAccesso;
import com.AbbonamentiPalestra.Repository.UtenteAccessoRepository;

@Service
public class UtenteAccessoService {

	 @Autowired UtenteAccessoRepository utenteAccessoRepo;

	 public boolean login(String username, String password) {
	    UtenteAccesso utente = utenteAccessoRepo.findByUsername(username);
	    	// Verifica se l'utente esiste e se la password è corretta
	    	return utente != null && utente.getPassword().equals(password);
	 }
	 
	 public boolean usernameExists(String username) {
	     return utenteAccessoRepo.findByUsername(username) != null;
	 }
	 
	 public void createTestUser(String username, String password) {
	        // Verifica se l'utente esiste già
	        if (!usernameExists(username)) {
	            // Se l'utente non esiste, crea un nuovo utente
	            UtenteAccesso utente = new UtenteAccesso();
	            utente.setUsername(username);
	            utente.setPassword(password);
	            utenteAccessoRepo.save(utente);
	        }
	  }	 
}

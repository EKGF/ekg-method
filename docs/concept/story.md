# Story

=== "Business & Management Audience"

    A Story --- in the context of a [Use Case](use-case.md) in the 
    [Use Case Tree](use-case-tree.md) --- defines a business requirement.                       
                                                                                                                            
    A business user could specify a requirement as follows:                                                                 
                                                                                                                            
    - _As the Chief Risk Officer, I need to know our current Risk Position against party B, so that I can Assess the Risk_    
    - _As an Auditor, I need to get a list of all current board members of legal entity X, so that I can Verify Stakeholders_ 
    - _As an Employee, I need to get a list of all my colleagues in my unit, so that I Know my Colleagues_                    
    - _As a customer, I need to get a list of all products, so that I can make a product selection_                           
                                                                                                                            
    And so forth. That's all we ask in the early phases of a given use case.                                                                                     
                                                                                                                            

=== "Data & Tech Audience"

    "User Stories" start out as plain English sentences that, as the name suggests, come from the user.
    In other words, "the Business" or "the Customer", the end user of a system or application, is
    responsible for explaining to the people who need to deliver that system what the system is supposed to do.                     
                                                                                                                     
    Makes sense right? Unfortunately, it's usually not that simple.
    All kinds of other factors come into play that have nothing to do with specifying what the user
    _really_ wants such as design, architecture, existing systems, budgets, time, regulations, policies 
    and technical capabilities.
                                                                                                                     
    However, it is a good thing to at least capture the "real" wishes of the user without having to consider all of 
    those other aspects.                                                                                            
    Where the challenge is to ask the user to step out of their normal day-to-day practices and comfort zone and to 
    think ahead in a way that is not restricted by all the daily hurdles and practicalities.                        
    This method proposes to use "Structured Business User Stories" to achieve many things such as:                  
                                                                                                                     
     * have a more strategic view on which functionality is ^^really^^ required                                          
     * allow to see "the disconnect" or "the gap" between what's required and what is currently available,
       delivered and deliverable                                                                                     
     * avoid "tunnel thinking" where everyone, especially also "the business" itself, makes all kinds of
       assumptions that may or may not be true and could severely diminish creativity.                               
     * create a clear separation of concerns: the business specifies what they need but leaves it to the
       data and technology people to work out how they can deliver it.
       So no more "screen designs" (that comes later) or "schema's" that are used as
       "functional specification".
       We need to be able to go deeper, to the core questions about **"what do you ^^really^^ need?"** 
       (and forget about the "How" for a minute).                                                                                
     * have clear testable specifications of required functionality for the whole life-cycle of a given              
       user story.<br/>                                                                                              
       As long as people need a given story to be implemented, it will continuously be tested "end-to-end",
       from inception all the way to production, not only before deployment into production but actually
       also in production itself.
       The EKG knows about "its Stories" and continuously tests them, it therefore knows about its own
       "functional health" and can detect whenever something changes (code, ontologies, ETL, new policies) 
       whether it can still deliver all functionality                                 
                                                                                                                     
    Here's a diagram that illustrates how we can break up a user story in some interesting components that
    we can link to other data structures in the Knowledge Graph such as a taxonomy of all ["Personas"](persona.md)

    <figure markdown>
      TODO
    </figure>
                                                                                                                     
    Here's one example of a User Story, more examples will follow later:                                            

    <figure markdown>
      TODO
    </figure>
                                                                                                                     
                                                                                                                     
